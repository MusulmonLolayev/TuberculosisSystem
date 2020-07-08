import Vue from 'vue'
import Vuex from 'vuex'
import Api from '../api/Api'

Vue.use(Vuex)


let store = new Vuex.Store ({
    state: {
        countries: [],
        regions: [],
        districts: [],
        occupations: [],
        token: localStorage.getItem('token') || '',
        user: {},
        patients: [],
        district: {},
        clinical_forms: [],
        localizations: [],
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
        SET_PATIETNS_TO_STATE: (state, patients) =>{
            state.patients = patients
        },
        SET_DISTRICT_TO_STATE: (state, district) =>{
            state.district = district
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
        SET_CLINICAL_FORMS_TO_STATE: (state, clinical_forms) => {
            state.clinical_forms = clinical_forms
        },
        SET_LOCALIZATION_TO_STATE: (state, localizations) => {
            state.localizations = localizations;
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
                resolve()
            })
        },

        GET_PATIETNS_FROM_API({commit}){
            return Api().get('/patients')
            .then((patients) => {
                commit('SET_PATIETNS_TO_STATE', patients.data);
                return patients;
            })
            .catch((error) => {
                console.log(error);
                return error;
            })
        },
        GET_DISTRICT_FROM_API({commit}, id){
            return Api().get('/districts/' + id)
            .then((response) =>{
                commit('SET_DISTRICT_TO_STATE', response.data)
                return response;
            })
            .catch((error) => {
                console.log(error)
                return error
            })
        },
        GET_CLINICAL_FORMS_FROM_API({commit}){
            return Api().get('/clinicalforms')
            .then((response) => {
                commit('SET_CLINICAL_FORMS_TO_STATE', response.data)
                return response
            })
            .catch((error) => {
                console.log(error)
                return error
            })
        },
        GET_LOCALIZATION_FROM_API({commit}){
            return Api().get('/localization')
            .then((response) => {
                commit('SET_LOCALIZATION_TO_STATE', response.data)
                return response
            })
            .catch((error) => {
                console.log(error)
                return error
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
        
        PATIENTS(state){
            return state.patients;
        },
        DISTRICT(state){
            return state.district;
        },
        CLINICAL_FORMS(state){
            return state.clinical_forms
        },
        LOCALIZATIONS(state){
            return state.localizations
        },
    }
});

export default store