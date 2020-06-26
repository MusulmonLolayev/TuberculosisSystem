import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

let store = new Vuex.Store ({
    state: {
        countries: [],
        regions: [],
        districts: [],
        occupations: [],
        token: localStorage.getItem('token') || '',
        user: {}
    },
    mutations: {
        SET_COUNTRIES_TO_STATE: (state, countries) =>{
            state.countries = countries
        },
        SET_REGIONS_TO_STATE: (state, regions) =>{
            state.regions = regions
        },
        SET_DISTRICTS_TO_STATE: (state, districts) =>{
            state.districts = districts
        },
        SET_OCCUPATIONS_TO_STATE: (state, occupation) =>{
            state.occupations = occupation
        },
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
          },
          auth_error(state){
            state.status = 'error'
          },
          logout(state){
            state.status = ''
            state.token = ''
          },
    },
    actions: {
        GET_COUNTRIES_FROM_API({commit}){
            return axios('http://127.0.0.1:8000/api/countries', {
                method: 'GET'
            })
            .then((countries) => {
                commit('SET_COUNTRIES_TO_STATE', countries.data);
                return countries;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
        },

        GET_REGIONS_FROM_API({commit}, url){
            return axios(url, {
                method: 'GET'
            })
            .then((regions) => {
                commit('SET_REGIONS_TO_STATE', regions.data);
                return regions;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
        },

        GET_DISTRICTS_FROM_API({commit}, url){
            return axios(url, {
                method: 'GET'
            })
            .then((districts) => {
                commit('SET_DISTRICTS_TO_STATE', districts.data);
                return districts;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
        },

        GET_OCCUPATIONS_FROM_API({commit}){
            return axios('http://127.0.0.1:8000/api/occupations', {
                method: 'GET'
            })
            .then((occupations) => {
                commit('SET_OCCUPATIONS_TO_STATE', occupations.data);
                return occupations;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
        },
        login({commit}, user){
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url: 'http://127.0.0.1:8000/api/login', data: user, method: 'POST'})
                .then(response => {
                    const token = response.data.token
                    const user = response.data.user

                    localStorage.setItem('token', token)
                    axios.defaults.headers.common['Authorization'] = token
                    commit('auth_success', token, user)
                    resolve(response)
                })
                .error(error => {
                    commit('auth_error')
                    localStorage.removeItem('token')
                    reject(error)
                })
            })
        },
        logout({commit}){
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        }
    },
    getters: {
        COUNTRIES(state){
            return state.countries;
        },
        REGIONS(state){
            return state.regions;
        },
        DISTRICTS(state){
            return state.districts;
        },
        OCCUPATIONS(state){
            return state.occupations;
        },
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    }
});

export default store