<template>
    <v-form v-model="valid" class="card-form">
        <step1 v-show="step_count == 1" ref="step1" :patient="patient"/>
        <step2 v-show="step_count == 2"/>
        <v-card-actions>
            <v-btn text v-on:click="btnSave">Save</v-btn>
            <v-btn text v-on:click="step_count--" :disabled="step_count <= 1">Back</v-btn>
            <v-btn text v-on:click="step_count++" :disabled="step_max < step_count">Next</v-btn>
        </v-card-actions>
    </v-form>
</template>

<script>
import step1 from './step1'
import step2 from './step2'
import axios from 'axios'

export default {
    components:{
        step1,
        step2
    },
    data: function(){
        return {
            step_count: 1,
            step_max: 1,
            patient: {
            }
        }
    },
    methods: {
        btnSave(){
            let patient = Object.assign({}, this.patient)

            //patient.occupation_id = patient.occupation.id
            patient.occupation = patient.occupation.id

            //patient.district_id = patient.district.id
            patient.district = patient.district.id
             
            axios.post('http://127.0.0.1:8000/api/patientcreate', {
                patient,
            })
            .then(function(response){
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            });
        }
    }
}
</script>