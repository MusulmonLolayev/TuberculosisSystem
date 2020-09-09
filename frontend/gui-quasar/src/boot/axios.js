import Vue from 'vue'
import axios from 'axios'

const axiosConfig = {
    baseURL: 'http://127.0.0.1:8000/api',
};

let axiosIstance = axios.create(axiosConfig)

export default ({store, Vue}) => {
    Vue.prototype.$axios = axiosIstance,
    store.$axios = axiosIstance
}