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
    }
});

export default store