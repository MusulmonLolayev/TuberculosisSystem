import axios from 'axios'

const axiosConfig = {
    baseURL: 'http://127.0.0.1:8000/api',
};

let Api = axios.create(axiosConfig)

export default ({store, Vue}) => {
    Vue.prototype.$axios = Api,
    store.$axios = Api
}