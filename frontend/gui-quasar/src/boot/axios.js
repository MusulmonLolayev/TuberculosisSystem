import axios from 'axios'

const axiosConfig = {
    baseURL: 'http://127.0.0.1:8000/api',
    headers: {
        Accept: "application/json", "Content-Type": "application/json"
    },
};

export const Api = axios.create(axiosConfig)

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
        if (error.config && error.response && error.response.status === 401){
          if (store.state.auth.access_token == null || typeof store.state.auth.access_token == 'undefined')
            router.push('/login')
          else{
            //console.log(store.state.refreshToken)
            if (store.state.auth.refresh_token != null && typeof store.state.auth.refresh_token != 'undefined')
                store.dispatch('auth/refresh_token')
            else
                router.push('/login')
          }
        }
        return Promise.reject(error);
    }),
    Vue.prototype.$axios = Api,
    store.$axios = Api
}