import axios from 'axios'
import createAuthRefreshInterceptor from 'axios'

const baseURL = 'http://127.0.0.1:8000/api'

const axiosConfig = {
    baseURL: baseURL,
    headers: {
        Accept: "application/json", "Content-Type": "application/json"
    },
};

let helper = true

export const Api = axios.create(axiosConfig)

const refreshAuthLogic = failedRequest => 
  Api.post('/login/refresh')
  .then(tokenRefreshResponse => {
    console.log(2222)
    localStorage.setItem("access_token", tokenRefreshResponse.data.token)
    failedRequest.response.config.headers['Authorization'] = 'Bearer ' + tokenRefreshResponse.data.token
    return Promise.resolve()
  })

//createAuthRefreshInterceptor(Api, refreshAuthLogic)

export default ({store, Vue, router}) => {
    Api.defaults.headers.common['Authorization'] = `Bearer ${store.state.auth.access_token}`,
    // Add a request interceptor
    Api.interceptors.request.use(function (config) {
        // Do something before request is sent
        //store.commit('LOADER', true)
        return config;
    }, function (error) {
    // Do something with request error
      //store.commit('LOADER', false)
      //store.state.message.showMessage(error, Helper.message_types.error)
      return Promise.reject(error);
    }),

    // Add a response interceptor
    Api.interceptors.response.use(function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data
        //store.commit('LOADER', false)
        return response;
      }, function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        //store.commit('LOADER', false)
        /*if (error.config && error.response && error.response.status === 401){
          if (store.state.auth.access_token == null || typeof store.state.auth.access_token == 'undefined')
            router.push('/login')
          else{
            //console.log(store.state.refreshToken)
            if (helper && error.response.data.code == 'token_not_valid' && store.state.auth.refresh_token != null && typeof store.state.auth.refresh_token != 'undefined'){
              helper = false
              delete Api.defaults.headers['common']
              console.log(Api.defaults.headers)
              console.log(error.response.data)
              Api.post('login/refresh', {
                refresh: store.state.auth.refresh_token
              })
              .then(response => {
                console.log(response.data)
              })
              //store.dispatch('auth/refresh_token')
            }
            else
                router.push('/login')
          }
        }*/
        return Promise.reject(error);
    }),
    Vue.prototype.$axios = Api,
    store.$axios = Api
}