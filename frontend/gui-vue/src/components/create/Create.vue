<template>
    <div>
        <v-stepper v-model="step_count"
            alt-labels
        >
            <v-stepper-header>
                <v-stepper-step editable step="1">            
                    Initial information
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :editable='!isValidate_step1' step="2">
                    Initial questions
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="3" :editable='!isValidate_step2'>Name of step 3</v-stepper-step>
            </v-stepper-header>

            <v-stepper-items>
                <v-stepper-content step="1">
                    <step1 :patient="patient"/>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <step2 />
                </v-stepper-content>

                <v-stepper-content step="3">
                
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>

        <div class="stepper-actions">
            <v-btn class="btn-actions"
                color="primary"
                @click="stepBack"
                :disabled='this.step_count == 1'
            >
                Back
            </v-btn>

            <v-btn
                color="primary"
                @click="stepContinue"
                :disabled='isValidate'
            >
                Continue
            </v-btn>

            <v-btn text>Cancel</v-btn>        
        </div>
    </div>
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
            step_max: 3,
            patient: {
            },
        }
    },
    computed:{
        isValidate_step1: function(){
            return true;
        },
        isValidate_step2: function(){
            return true;
        },
        isValidate_step3: function(){
            return true;
        },
        isValidate: function(){
            return this.isValidate_step1 && this.isValidate_step2 && this.isValidate_step3
        },
        
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
        },
        stepBack(){
            if (this.step_count > 1){
                this.step_count--;
                console.log(this.step_count)
            }
                
        },
        stepContinue(){
            if (this.step_count < this.step_max){
                this.step_count++;
                console.log(this.step_count)
            }
        }
    }
}
</script>

<style scoped>
    .stepper-actions{
        margin: 10px;
    }
    .btn-actions{
        margin: 10px;
    }
</style>