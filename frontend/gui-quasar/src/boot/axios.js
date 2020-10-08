import axios from 'axios'
import createAuthRefreshInterceptor from 'axios'

const baseURL = 'http://127.0.0.1:8000/api'

const axiosConfig = {
  baseURL: baseURL,
  headers: {
    Accept: "application/json", "Content-Type": "application/json"
  },
};

export const Api = axios.create(axiosConfig)

function refreshToken(store) {
  const refreshingCall = Api.post('/login/refresh', {
    refresh: store.state.auth.refresh_token
  })
    .then(response => {
      store.dispatch('auth/refresh_token',
        {
          access: response.data.access
        })
      store.dispatch('common/setIsRefreshingTokenExpired', {status: false})
      return Promise.resolve(true)
    })
    .catch(() => {
      return Promise.reject()
    })
  return refreshingCall
}

let Is_Refreshed_Token = false

export default ({ store, Vue, router }) => {
  Api.defaults.headers.common['Authorization'] = `Bearer ${store.state.auth.access_token}`,
    Vue.prototype.$axios = Api,
    store.$axios = Api,
    Api.interceptors.response.use(response => response,
      function (error) {
        let data = error.response.data
        if (!Is_Refreshed_Token &&
          error.response.status === 401 && 
          data && data.code && data.code == "token_not_valid" && 
          store.state.auth.refresh_token) {
            Is_Refreshed_Token = true
          return refreshToken(store).then(_ => {
            error.config.headers['Authorization'] = 'Bearer ' + store.state.auth.access_token;
            error.config.baseURL = undefined;
            return Api.request(error.config);
          })
          .catch(() => {
            return Promise.reject(true)
          })
        }
        else{
          if (Is_Refreshed_Token) {
            store.dispatch('common/setIsRefreshingTokenExpired', {status: true})
            router.push('/login')
          }
          else{

          }
        } 
      }
    )
}