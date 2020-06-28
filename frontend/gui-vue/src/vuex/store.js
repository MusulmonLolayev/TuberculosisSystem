import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Api from '../api/Api'
//import jwt_decode from 'jwt-decode';

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
            return Api().get('/countries')
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
            return Api().get(url)
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
            return Api().get(url)
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
            return Api().get('/occupations')
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
                Api().post('/login', {user})
                .then(response => {
                    const token = response.data.token
                    const user = response.data.user

                    localStorage.setItem('token', token)
                    axios.defaults.headers.common['Authorization'] = token
                    commit('auth_success', token, user)
                    resolve(response)
                })
                .catch(error => {
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
        },
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