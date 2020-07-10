<template>
    <div>
        <MessageBox :data='message'/>
        <v-stepper
            alt-labels
            v-model="step_count"
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
                :disabled='!(step_count > 1)'
            >
                Back
            </v-btn>

            <v-btn
                color="primary"
                @click="stepContinue"
                :disabled='!(step_count < step_max)'
            >
                Continue
            </v-btn>

            <v-btn text @click="btnCancel">Cancel</v-btn>

            <v-btn text @click="btnSave" color="primary" v-bind:disabled='!settings.IsUpdated'>Save</v-btn>
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
import MessageBox from '../commons/messagebox'
import MessgeBox_Class from '../commons/messagebox_class'

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
        Other,
        MessageBox,
    },
    data: function(){
        return {
            settings: {
                IsUpdated: false,
            },
            step_count: 1,
            step_max: 5,
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
            message: new MessgeBox_Class()
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
        btnCanelingAgree(){
            console.log('btnCanelingAgree')
            this.$router.go(-1)
        },
        SavePatient(){
            try{
                let patient = this.patient
                // Check this patient has id which means that the patient was created in database
                // if id is undefined then create object, otherwise edit it
                if (typeof patient.id == 'undefined'){
                    Api().post('/patient_request', {
                        patient,
                    })
                    .then(function(response){
                        patient.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')
                    })
                }
                else{
                    Api().put('/patient_request', {
                        patient,
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
            }
            catch(e){
                console.log(e)
                this.message.showMessage('Error', 'Error text: ' + e, 'error')
            }
        },
        async SaveQuestions(){

        },
        async SavePrimaryDiagnose(){
            try{

                // Check this patient has id which means that the patient was created in database
                // if id is undefined then create object
                if (typeof this.patient.id == 'undefined'){
                    await this.SavePatient()
                }

                // Chech the primary diagnose id to be undefined to know ethier create instane or edit
                this.primarydiagnose.patient = this.patient.id
                let primarydiagnose = this.primarydiagnose
                
                if (typeof primarydiagnose.id == 'undefined'){
                    await Api().post('/primary_request', {
                        primarydiagnose
                    })
                    .then(function(response){
                        console.log(response)
                        primarydiagnose.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/primary_request', {
                        primarydiagnose
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
            }
            catch(e){
                console.log(e)
                this.message.showMessage('Error', 'Error text: ' + e, 'error')
            }
        },
        async SaveTakingMedicineAndComplaint(){
            try{

                // Check this patient has id which means that the patient was created in database
                // if id is undefined then create object
                if (typeof this.patient.id == 'undefined'){
                    await this.SavePatient()
                }

                // Check the primary diagnose id to be undefined to know ethier create instane or edit
                this.takingmedicine.patient = this.patient.id
                let takingmedicine = this.takingmedicine
                
                if (typeof takingmedicine.id == 'undefined'){
                    await Api().post('/taking_request', {
                        takingmedicine
                    })
                    .then(function(response){
                        console.log(response)
                        takingmedicine.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/taking_request', {
                        takingmedicine
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }

                // Complaint
                this.complaint.patient = this.patient.id
                let complaint = this.complaint
                if (typeof complaint.id == 'undefined'){
                    await Api().post('/complaint_request', {
                        complaint
                    })
                    .then(function(response){
                        console.log(response)
                        complaint.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/complaint_request', {
                        complaint
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
            }
            catch(e){
                console.log(e)
                this.message.showMessage('Error', 'Error text: ' + e, 'error')
            }
        },
        async SaveBloodImmunogramAndOther(){
            try{

                // Check this patient has id which means that the patient was created in database
                // if id is undefined then create object
                if (typeof this.patient.id == 'undefined'){
                    await this.SavePatient()
                }

                // Check the blood id to be undefined to know ethier create instane or edit
                this.bloodanalysis.patient = this.patient.id
                let bloodanalysis = this.bloodanalysis
                
                if (typeof bloodanalysis.id == 'undefined'){
                    await Api().post('/blood_request', {
                        bloodanalysis
                    })
                    .then(function(response){
                        console.log(response)
                        bloodanalysis.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/blood_request', {
                        bloodanalysis
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }

                // immunogram
                this.immunogram.patient = this.patient.id
                let immunogram = this.immunogram
                if (typeof immunogram.id == 'undefined'){
                    await Api().post('/immunogram_request', {
                        immunogram
                    })
                    .then(function(response){
                        console.log(response)
                        immunogram.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/immunogram_request', {
                        immunogram
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }

                // other
                this.other.patient = this.patient.id
                let other = this.other
                if (typeof other.id == 'undefined'){
                    await Api().post('/other_request', {
                        other
                    })
                    .then(function(response){
                        console.log(response)
                        other.id = response.data
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
                else{
                    await Api().put('/other_request', {
                        other
                    })
                    .then(function(response){
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e)
                        this.message.showMessage('Error', 'Error text: ' + e, 'error')        
                    })
                }
            }
            catch(e){
                console.log(e)
                this.message.showMessage('Error', 'Error text: ' + e, 'error')
            }
        },
        async btnSave(){
            //this.message.showMessage('Saving data', 'Do you want to save data?', 'success', true, this.btnSavingAgree)
            console.log(this.step_count)
            switch (this.step_count){
                case 1: this.SavePatient(); break;
                case 2: this.SaveQuestions(); break;
                case 3: this.SavePrimaryDiagnose(); break;
                case 4: this.SaveTakingMedicineAndComplaint(); break;
                case 5: this.SaveBloodImmunogramAndOther(); break;
            }            
        },
        stepBack(){
            if (this.step_count > 1){
                this.step_count--;
            }
                
        },
        stepContinue(){
            if (this.step_count < this.step_max){
                this.step_count++;
            }
        },
        btnCancel(){
            if (this.settings.IsUpdated){
                this.message.showMessage('Canceling', 'Do you want to cancel creating? You have some creating data.', 'warning', true, this.btnCanelingAgree)
            }
            else{
                this.btnCanelingAgree()
            }
        },
    },
    updated: function(){
        this.settings.IsUpdated = true
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