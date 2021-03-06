<template>
  <div>
    <v-stepper alt-labels v-model="step_count" :vertical="vertical">
      <template v-if="vertical">
        <template v-for="(item, index) in stepper_data">
          <v-stepper-step :key="'V' + index" step="index" :editable="item.editable">{{item.title}}</v-stepper-step>
        </template>
      </template>
      <template v-else>
        <v-stepper-header>
          <template v-for="(item, index) in stepper_data">
            <v-stepper-step :key="'H' + index" :step="index" :editable="item.editable">{{ item.title }}</v-stepper-step>
            <v-divider v-if="index != 6" :key="index"></v-divider>
          </template>
        </v-stepper-header>
      </template>
      <v-stepper-items>
        <v-stepper-content step="0">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-patient ref="PatientForm" :patient="patient" :check_acceptability="check_acceptability"/>
          </div>
        </v-stepper-content>

        <v-stepper-content step="1">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-initial-question :selected="initial_question_selected" />
          </div>
        </v-stepper-content>

        <v-stepper-content step="2">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-primary-diagnose :primarydiagnose="primarydiagnose" />
          </div>
        </v-stepper-content>

        <v-stepper-content step="3">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-taking-medicine :takingmedicine="takingmedicine" />
          </div>
        </v-stepper-content>

        <v-stepper-content step="4">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-complaint :complaint="complaint" />
          </div>
        </v-stepper-content>

        <v-stepper-content step="5">
          <div style="margin-left: 20px; margin-right: 20px">
            <v-blood-analysis :bloodanalysis="bloodanalysis" ref="BloodAnalysis" :check_acceptability="check_acceptability"/>
          </div>
        </v-stepper-content>

        <v-stepper-content step="6">
          <div style="margin-left: 20px; margin-right: 20px">
            <div>
              <v-other :other="other" />
            </div>
          </div>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>

    <div class="stepper-actions">
      <v-btn
        class="btn-actions"
        color="primary"
        @click="stepBack"
        :disabled="!(step_count > 0)"
      >Back</v-btn>

      <v-btn color="primary" @click="stepContinue" :disabled="!(step_count < step_max)">Continue</v-btn>

      <v-btn text @click="btnCancel" color='red'>Cancel</v-btn>

      <v-btn text @click="btnSave" color="primary" v-bind:disabled="!settings.IsUpdated">Save</v-btn>
      <v-btn text @click="btnNew" color="primary" :disabled="settings.IsNew">New patient</v-btn>
    </div>
  </div>
</template>

<script>
import vPatient from "./v-patient";
import vInitialQuestion from "./v-initial-question";
import vPrimaryDiagnose from "./v-primary-diagnose";
import vTakingMedicine from "./v-taking-medicine";
import vComplaint from "./v-complaint";
import vBloodAnalysis from "./v-blood-analysis";
import vOther from "./v-other";
import Helper from "../commons/functions.js"

import {Api} from "@/api/Api";

export default {
  name: "v-create",
  components: {
    vPatient,
    vInitialQuestion,
    vPrimaryDiagnose,
    vTakingMedicine,
    vComplaint,
    vBloodAnalysis,
    vOther,
  },
  data: function() {
    return {
      vertical: false,
      stepper_data: [
        {
          step: 1,
          editable: true,
          title: "Initial information"
        },
        {
          step: 2,
          editable: true,
          title: "Initial questions"
        },
        {
          step: 3,
          editable: true,
          title: "Primary diagnose"
        },
        {
          step: 4,
          editable: true,
          title: "Taking medicine"
        },
        {
          step: 5,
          editable: true,
          title: "Complaint"
        },
        {
          step: 6,
          editable: true,
          title: "Blood analysis"
        },
        {
          step: 8,
          editable: true,
          title: "Others"
        }
      ],
      settings: {
        IsUpdated: false,
        IsNew: true
      },
      step_count: 0,
      step_max: 6,
      patient: {
      },
      initial_question_selected: {
        checkbox: [],
        radio: {}
      },
      initial_question: {},
      primarydiagnose: {},
      takingmedicine: {},
      complaint: {},
      bloodanalysis: {},
      other: {},
      ranges: ''
    };
  },
  computed: {
    isValidate_step1: function() {
      return false;
    },
    isValidate_step2: function() {
      return false;
    },
    isValidate_step3: function() {
      return false;
    },
    isValidate: function() {
      return false;
      //return this.isValidate_step1 && this.isValidate_step2 && this.isValidate_step3
    },
    /*vertical: function() {
      return window.innerWidth < 640;
    }*/
    IsNew: function(){
      return this.patient.id != 'undefined'
    }
  },
  methods: {
    async initialize() {
      // Must to do after all
      this.ranges = (await Api.get("/getaccetableintervals")).data
    },
    btnCanelingAgree() {
      this.$router.go(-1);
    },
    DealSavingRespone(response){
      if (response == true){
        this.$store.state.message.showMessage('Action was successfully', Helper.message_types.success)
      }
      else{
        this.$store.state.message.showMessage('Action was unsuccessfully\n' + response, 
        Helper.message_types.error, 10000)
      }
    },
    async SavePatient() {
      if (this.$refs['PatientForm'].hasError()){
        this.$store.state.message.showMessage('Error, please fill all the required fields in initial information', 
        Helper.message_types.error)
        this.step_count = 0
        return 0
      }
      let response = await Helper.saveInstance(this.patient, '/patient_request')
      this.DealSavingRespone(response)
    },
    async SaveInitialQuestions() {
      //console.log(Object.values(this.initial_question_selected.radio))
      try {
        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }

        // Chech the primary diagnose id to be undefined to know ethier create instane or edit
        this.initial_question.patient = this.patient.id;
        // Convert the ids into text
        this.initial_question.questions = ""
        this.initial_question_selected.checkbox.map(item => {
          this.initial_question.questions += item + ","
        })
        Object.values(this.initial_question_selected.radio).map(item => {
          this.initial_question.questions += item + ","
        })
        // Clean the last mark (,)
        this.initial_question.questions = this.initial_question.questions.slice(0, -1)
        // For test Patient 70 id
        //this.initial_question.patient = 70
        //return 0;
        
        let response = await Helper.saveInstance(this.initial_question, '/initial_question_request')
        this.DealSavingRespone(response)
      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    async SavePrimaryDiagnose() {
      try {
        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }

        // Chech the primary diagnose id to be undefined to know ethier create instane or edit
        this.primarydiagnose.patient = this.patient.id;
        // For test Patient 70 id
        //this.primarydiagnose.patient = 70;

        let response = await Helper.saveInstance(this.primarydiagnose, '/primary_request')
        this.DealSavingRespone(response)        

      } catch (e) {
        console.log(e);
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    async SaveTakingMedicine() {
      try {
        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }

        // Check the primary diagnose id to be undefined to know ethier create instane or edit
        this.takingmedicine.patient = this.patient.id;
        // For test patient id = 70
        // this.takingmedicine.patient = 70;

        let response = await Helper.saveInstance(this.takingmedicine, '/taking_request')
        this.DealSavingRespone(response)
      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    async SaveComplaint() {
      try {
        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }
        // Complaint
        this.complaint.patient = this.patient.id;
        // For test Patient id = 70
        //this.complaint.patient = 70;
        
        let response = await Helper.saveInstance(this.complaint, '/complaint_request')
        this.DealSavingRespone(response)

      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    async SaveBlood() {
      try {

        if (this.$refs['BloodAnalysis'].hasError()){
          this.$store.state.message.showMessage('Error, please fill all the required fields in initial information', 
          Helper.message_types.error)
          this.step_count = 5
          return 0
        }

        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }

        // Check the blood id to be undefined to know ethier create instane or edit
        this.bloodanalysis.patient = this.patient.id;
        // For test pateint id = 70
        //this.bloodanalysis.patient = 70

        let response = await Helper.saveInstance(this.bloodanalysis, '/blood_request')
        this.DealSavingRespone(response)

      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    async SaveOther() {
      try {
        // Check this patient has id which means that the patient was created in database
        // if id is undefined then create object
        if (typeof this.patient.id == "undefined") {
          await this.SavePatient();
        }

        // other
        this.other.patient = this.patient.id;
        // For test Patient id = 70
        //this.other.patient = 70;
        
        let response = await Helper.saveInstance(this.other, '/other_request')
        this.DealSavingRespone(response)
        
      } catch (e) {
        this.$store.state.message.showMessage("Error", e, "error");
      }
    },
    btnSave() {
      switch (this.step_count) {
        case 0:
          this.SavePatient();
          break;
        case 1:
          this.SaveInitialQuestions();
          break;
        case 2:
          this.SavePrimaryDiagnose();
          break;
        case 3:
          this.SaveTakingMedicine();
          break;
        case 4:
          this.SaveComplaint();
          break;
        case 5:
          this.SaveBlood();
          break;
        case 6:
          this.SaveOther();
          break;
      }
      this.settings.IsNew = false
    },
    stepBack() {
      if (this.step_count > 0) {
        this.step_count--;
      }
    },
    stepContinue() {
      if (this.step_count < this.step_max) {
        this.step_count++;
      }
    },
    btnCancel() {
      this.$refs['message'].showMessage(
        "Canceling",
        "Do you want to cancel creating? You have some created data.",
        "warning",
        true,
        this.btnCanelingAgree
      );
    },
    btnNew(){
      this.settings.IsNew = true
      delete this.patient.id
      this.patient.last_name = ''
      this.patient.first_name = ''
      this.patient.middle_name = ''
    },
    check_acceptability: function(name, instance){
      return Helper.check_acceptability(name, instance, this.ranges)
    }
  },
  updated: function() {
    this.settings.IsUpdated = true;
  },
  mounted: function(){
    this.initialize()
  }
};
</script>

<style scoped>
.stepper-actions {
  margin: 10px;
}
.btn-actions {
  margin: 10px;
}
</style>