<template>
        <v-container>
            <v-row>
                <v-col cols="10" md="3">
                    <v-text-field
                        label="Last name"
                        v-model="patient.last_name"
                        required/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        label="First name"
                        v-model="patient.first_name"
                        required />
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        label="Middle name"
                        v-model="patient.middle_name"
                        />
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='Date of birthday' :date="patient_edit.birthday" :change="birthdayChange"/>
                </v-col>

                <v-col cols="10" md="3">
                    <v-radio-group row v-model="gender" @change='rbChange'>
                        <v-radio label="Male" :value="0" />
                        <v-radio label="Female" :value="1"/>
                    </v-radio-group>
                </v-col>
            </v-row>
            
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
                        v-model="selectedReigion"
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
                        required
                        v-model="patient.address"/>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="10" md="3">
                    <datepicker label='From date' :date="patient_edit.fromdate" :change="fromdateChange"/>
                </v-col>
                
                <v-col cols="10" md="3">
                    <v-select
                        label="Occupation" 
                        :items="OCCUPATIONS"
                        item-text='title'
                        return-object
                        item-value="id"
                        v-model="patient.occupation" />
                </v-col>

                <v-col cols="10" md="3">
                    <v-text-field
                        label="Number"
                        required
                        v-model="patient.number"/>
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
    props: ['patient'],
    data: function(){
        return {
            patient_edit: {
                birthday: {
                    'value': this.patient.birthday
                },
                fromdate: {
                    'value': this.patient.fromdate
                },
            },
            selectedCountry: {},
            selectedReigion: {},
            selectedDistrict: {},
            gender: 0
        }
    },
    computed: {
        ...mapGetters([
            'COUNTRIES', 
            'REGIONS',
            'DISTRICTS',
            'OCCUPATIONS',
            'DISTRICT',
        ]),
    },
    methods: {
        ...mapActions([
            'GET_COUNTRIES_FROM_API',
            'GET_REGIONS_FROM_API',
            'GET_DISTRICTS_FROM_API',
            'GET_OCCUPATIONS_FROM_API',
            'GET_DISTRICT_FROM_API',
        ]),

        CountryChanged(a){
            var url = "/regions_by_country/" + a.id
            this.GET_REGIONS_FROM_API(url);
        },
        RegionChanged(a){
            var url = "/districts_by_region/" + a.id
            this.GET_DISTRICTS_FROM_API(url);
        },
        birthdayChange(){
            this.patient.birthday = this.patient_edit.birthday.value
        },
        fromdateChange(){
            this.patient.fromdate = this.patient_edit.fromdate.value
        },
        rbChange(e){
            this.patient.gender = e == 0 ? true : false
        }

    },
    mounted(){
        this.GET_COUNTRIES_FROM_API()
        this.GET_OCCUPATIONS_FROM_API()
        
        // Setting defualt values when it is been edited
        if (typeof this.patient.id != 'undefined'){
            // select region, country and district by patient for editing
            this.selectedCountry = this.DISTRICT.region.country.id
            // when the country changes then must notice about it by calling the method.
            this.CountryChanged(this.DISTRICT.region.country)
            
            this.selectedReigion = this.DISTRICT.region.id
            // it is as same as the country selection
            this.RegionChanged(this.DISTRICT.region)

            this.selectedDistrict = this.DISTRICT.id

            // set gender
            this.gender = this.patient.gender == true ? 0 : 1
        }
    },
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