import Vue from 'vue'
import Vuex from 'vuex'
import {Api} from '../api/Api'
import Helper from '../components/commons/functions.js'

Vue.use(Vuex)

let store = new Vuex.Store({
    state: {
        countries: [],
        regions: [],
        districts: [],
        occupations: [],
        patients: [],
        district: {},
        clinical_forms: [],
        localizations: [],
        prevalences: [],
        character_stools: [],
        loader: false,
        message: null,
        alert: null,
        nav_title: 'Tuberculosis diagnostic system',
        token: localStorage.getItem('token') || null,
        refreshToken: localStorage.getItem('refreshToken') || null,
    },
    mutations: {
        SET_COUNTRIES_TO_STATE: (state, countries) => {
            state.countries = countries
        },
        SET_REGIONS_TO_STATE: (state, regions) => {
            state.regions = regions
        },
        SET_DISTRICTS_TO_STATE: (state, districts) => {
            state.districts = districts
        },
        SET_OCCUPATIONS_TO_STATE: (state, occupation) => {
            state.occupations = occupation
        },
        SET_PATIETNS_TO_STATE: (state, patients) => {
            state.patients = patients
        },
        SET_DISTRICT_TO_STATE: (state, district) => {
            state.district = district
        },
        auth_success(state, {access, refresh}) {
            state.status = 'success'
            state.token = access
            state.refreshToken = refresh
            //console.log(refresh)
            localStorage.setItem('token', access)
            localStorage.setItem('refreshToken', refresh)
        },
        auth_error(state, error) {
            state.message.showMessage(error, Helper.message_types.error)
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        updateAccess(state, access){
            state.token = access
            localStorage.setItem('token', access)
            Api.defaults.headers.common['Authorization'] = `Bearer ${access}`
        },
        SET_CLINICAL_FORMS_TO_STATE: (state, clinical_forms) => {
            state.clinical_forms = clinical_forms
        },
        SET_LOCALIZATION_TO_STATE: (state, localizations) => {
            state.localizations = localizations;
        },
        SET_PREVALENCES_TO_STATE: (state, prevalences) => {
            state.prevalences = prevalences
        },
        SET_CHARACTER_STOOLS_TO_STATE: (state, characters) => {
            state.character_stools = characters
        },
        LOADER(state, payload){
            state.loader = payload
        }
    },
    actions: {
        GET_COUNTRIES_FROM_API({ commit }) {
            if (this.state.countries.length == 0)
                return Api.get('/countries')
                    .then((countries) => {
                        commit('SET_COUNTRIES_TO_STATE', countries.data);
                        return countries;
                    })
                    .catch((error) => {
                        console.log(error);
                        return error;
                    })
            else return true
        },
        GET_REGIONS_FROM_API({ commit }, url) {
            return Api.get(url)
                .then((regions) => {
                    commit('SET_REGIONS_TO_STATE', regions.data);
                    return regions;
                })
                .catch((error) => {
                    console.log(error);
                    return error;
                })
        },
        GET_DISTRICTS_FROM_API({ commit }, url) {
            return Api.get(url)
                .then((districts) => {
                    commit('SET_DISTRICTS_TO_STATE', districts.data);
                    return districts;
                })
                .catch((error) => {
                    console.log(error);
                    return error;
                })
        },
        GET_OCCUPATIONS_FROM_API({ commit }) {
            if (this.state.occupations.length == 0)
                return Api.get('/occupations')
                    .then((occupations) => {
                        commit('SET_OCCUPATIONS_TO_STATE', occupations.data);
                        return occupations;
                    })
                    .catch((error) => {
                        console.log(error);
                        return error;
                    })
            else return true
        },
        login({ commit }, user) {
            return Api.post('/login', {
                username: user.username,
                password: user.password
            })
            .then(response => {
                //console.log(response.data.refresh)
                commit('auth_success', {access: response.data.access, refresh: response.data.refresh})
                Api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`
                return true
            })
            .catch((error) => {
                commit('auth_error', error)
            })
        },
        logout({ commit }) {
            commit('logout')
            localStorage.removeItem('token')
            Api.defaults.headers.common['Authorization'] = null
            return true
        },
        refreshToken({commit}){
            Api.post('/login/refresh', {
                refresh: this.state.refreshToken
            })
            .then((response) => {
                commit('updateAccess', response.data.access)
            })
            .catch((error) => {
                console.log(error)
            })
        },
        GET_PATIETNS_FROM_API({ commit }) {
            return Api.get('/patient_request')
                .then((patients) => {
                    commit('SET_PATIETNS_TO_STATE', patients.data);
                    return patients;
                })
                /*.catch((error) => {
                    console.log(error);
                    return error;
                })*/
        },
        GET_DISTRICT_FROM_API({ commit }, id) {
            return Api.get('/districts/' + id)
                .then((response) => {
                    commit('SET_DISTRICT_TO_STATE', response.data)
                    return response;
                })
                .catch((error) => {
                    console.log(error)
                    return error
                })
        },
        GET_CLINICAL_FORMS_FROM_API({ commit }) {
            if (this.state.clinical_forms.length == 0)
                return Api.get('/clinicalforms')
                    .then((response) => {
                        commit('SET_CLINICAL_FORMS_TO_STATE', response.data)
                        return response
                    })
                    .catch((error) => {
                        console.log(error)
                        return error
                    })
            else return true
        },
        GET_LOCALIZATION_FROM_API({ commit }) {
            if (this.state.localizations.length == 0)
                return Api.get('/localization')
                    .then((response) => {
                        commit('SET_LOCALIZATION_TO_STATE', response.data)
                        return response
                    })
                    .catch((error) => {
                        console.log(error)
                        return error
                    })
            else return true
        },
        GET_PREVALENCES_FROM_API({ commit }) {
            if (this.state.prevalences.length == 0)
                return Api.get('/prevalence')
                    .then((response) => {
                        commit('SET_PREVALENCES_TO_STATE', response.data)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            else return true
        },
        GET_CHARACTER_STOOL_FROM_API({ commit }) {
            if (this.state.character_stools.length == 0)
                return Api.get('/characterofstool')
                    .then((response) => {
                        commit('SET_CHARACTER_STOOLS_TO_STATE', response.data)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            else return true
        },
        SET_TOKEN(){
            if (this.state.token != null && typeof this.state.token != 'undefined'){
                Api.defaults.headers.common['Authorization'] = `Bearer ${this.state.token}`
            }
        }
    },
    getters: {
        COUNTRIES(state) {
            return state.countries;
        },
        REGIONS(state) {
            return state.regions;
        },
        DISTRICTS(state) {
            return state.districts;
        },
        OCCUPATIONS(state) {
            return state.occupations;
        },

        isLoggedIn(state){
            if (state.token != null && typeof state.token != 'undefined')
                return true
            return false
        },

        PATIENTS(state) {
            return state.patients;
        },
        DISTRICT(state) {
            return state.district;
        },
        CLINICAL_FORMS(state) {
            return state.clinical_forms
        },
        LOCALIZATIONS(state) {
            return state.localizations
        },
        PREVALENCES(state) {
            return state.prevalences
        },
        CHARACTER_STOOLS(state) {
            return state.character_stools
        }
    }
});

export default store