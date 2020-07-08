<template>
    <div>
        <v-stepper
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

                <v-stepper-step step="3" :editable='!isValidate_step2'>
                    Primary diagnose
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="4" editable>
                    Taking medicine and Complaint
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="5" editable>
                    Blood, immunogram analysis and others
                </v-stepper-step>
            </v-stepper-header>

            <v-stepper-items>
                
                <v-stepper-content step="1">
                    <PatientCard :patient="patient"/>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <step2 />
                </v-stepper-content>

                <v-stepper-content step="3">
                    <PrimaryDiagnose :primarydiagnose='primarydiagnose'/>
                </v-stepper-content>

                <v-stepper-content step="4">
                    <v-container>
                        <v-row>
                            <TakingMedicine :takingmedicine='takingmedicine'/>
                        </v-row>
                        <v-row>
                            <Complaint :complaint='complaint'/>
                        </v-row>
                    </v-container>
                </v-stepper-content>

                <v-stepper-content step="5">
                    <v-container>
                        <v-row>
                            <BloodAnalysis :bloodanalysis='bloodanalysis'/>
                        </v-row>
                        <v-row>
                            <Immunogram :immunogram='immunogram'/>
                        </v-row>
                        <v-row>
                            <Other :other='other' />
                        </v-row>
                    </v-container>
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
import PatientCard from './patient'
import step2 from './step2'
import PrimaryDiagnose from './primarydiagnose'
import TakingMedicine from './takingmedicine'
import Complaint from './complaint'
import BloodAnalysis from './bloodanalysis'
import Immunogram from './immunogram'
import Other from './other'
import Api from '@/api/Api'

export default {
    components:{
        PatientCard,
        step2,
        PrimaryDiagnose,
        TakingMedicine,
        Complaint,
        BloodAnalysis,
        Immunogram,
        Other
    },
    data: function(){
        return {
            step_count: 1,
            step_max: 3,
            patient: {
            },
            clinicalform: {

            },
            primarydiagnose: {

            },
            takingmedicine: {

            },
            complaint: {

            },
            bloodanalysis: {

            },
            immunogram: {

            },
            other: {

            },
        }
    },
    computed:{
        isValidate_step1: function(){
            return false
        },
        isValidate_step2: function(){
            return false
        },
        isValidate_step3: function(){
            return false
        },
        isValidate: function(){
            return false
            //return this.isValidate_step1 && this.isValidate_step2 && this.isValidate_step3
        },
        
    },
    methods: {
        btnSave(){
            let patient = this.patient
             
            Api.post('/patientcreate', {
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