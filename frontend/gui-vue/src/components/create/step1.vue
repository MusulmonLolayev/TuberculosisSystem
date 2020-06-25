<template>
        <v-container>
            <h1>Step1: Initial information</h1>
            <v-row>
                <v-col cols="10" md="3">
                    <v-text-field
                        label="Last name"
                        required/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        label="First name"
                        required />
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        label="Middle name"
                        required />
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='Date of birthday'/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-radio-group row>
                        <v-radio label="Male" value="radio-1" />
                        <v-radio label="Female" value="radio-2" />
                    </v-radio-group>
                </v-col>
            </v-row>
            
            <h2>Address</h2>
            <v-row>
                <v-col cols="10" md="3">
                    <v-select
                        label="Country" 
                        :items="COUNTRIES"
                        item-text='name'
                        v-on:change="CountryChanged"
                        return-object
                        item-value="id"
                        v-model="selectedCountry"
                        />
                </v-col>
                
                <v-col cols="10" md="3">
                    <v-select
                        label="Region"
                        :items="REGIONS"
                        item-text='name'
                        v-on:change="RegionChanged"
                        return-object
                        item-value="id"
                        v-model="selectedRegion"
                        />
                </v-col>
                <v-col cols="10" md="3">
                    <v-select
                        label="District" 
                        :items="DISTRICTS"
                        item-text='name'
                        return-object
                        item-value="id"
                        v-model="selectedDistrict"
                        />
                </v-col>

                <v-col cols="10" md="9">
                    <v-text-field
                        label="Address line"
                        required/>
                </v-col>
            </v-row>

            <h2>Addinational information</h2>
            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='Date of birthday'/>
                </v-col>
                
                <v-col cols="10" md="3">
                    <v-select
                        label="Occupation" 
                        :items="OCCUPATIONS"
                        item-text='title'
                        return-object
                        item-value="id"
                        v-model="selectedOccupation" />
                </v-col>
            </v-row>
        </v-container>
</template>

<script>
import datepicker from '../inputs/datepicker'
import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'step1',
    components: {
        datepicker,
    },
    props: {},
    data(){
        return {
            lastname: '',
            firstname: '',
            middlename: '',
            birthday: new Date(),
            gender: 1,
            selectedCountry: {},   
            selectedRegion: {},
            selectedDistrict: {},
            selectedOccupation: {}            
        }
    },
    computed: {
        ...mapGetters([
            'COUNTRIES'
        ]),
        ...mapGetters([
            'REGIONS'
        ]),
        ...mapGetters([
            'DISTRICTS'
        ]),
        ...mapGetters([
            'OCCUPATIONS'
        ]),
    },
    methods: {
        ...mapActions([
            'GET_COUNTRIES_FROM_API'
        ]),
        ...mapActions([
            'GET_REGIONS_FROM_API'
        ]),
        ...mapActions([
            'GET_DISTRICTS_FROM_API'
        ]),

        ...mapActions([
            'GET_OCCUPATIONS_FROM_API'
        ]),

        CountryChanged(a){
            var url = "http://127.0.0.1:8000/api/regions/" + a.id
            this.GET_REGIONS_FROM_API(url);
        },
        RegionChanged(a){
            var url = "http://127.0.0.1:8000/api/districts/" + a.id
            this.GET_DISTRICTS_FROM_API(url);
        },

    },
    mounted(){
        this.GET_COUNTRIES_FROM_API()
        this.GET_OCCUPATIONS_FROM_API()
    }
}
</script>


<style scoped>
    .card-form {
        margin:auto;
        margin-top:50px;
        max-width: 850px;
        width: 100%;
        border-radius: 10px;
        padding: 10px;
        float: center;
    }
    .header{
        align-content: center;
    }
    label{
        margin: 10px;
        margin-inline: initial;
    }
</style>