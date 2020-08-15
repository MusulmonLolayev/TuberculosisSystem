<template>
  <div>
    <v-message-box ref="message" />
    <v-expansion-panels v-model="panel" focusable multiple hover popout>
      <v-alert-box ref='alert' />
      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>General information</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row>
            <v-patient :patient="patient" />
          </v-row>
          <v-row>
            <v-col>
              <v-btn text @click="btnDelete">Delete</v-btn>
              <v-btn text @click="btnSave">Save</v-btn>
            </v-col>
          </v-row>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Initial question</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-initial-question-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Primary diagonose</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-primary-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Taking medicine</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-taking-medicine-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Complaint</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-complaint-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Blood</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-blood-table :patient="patient" :check_acceptability='check_acceptability'/>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Others</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-other-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import vPatient from "../create/v-patient";
import {Api} from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import vPrimaryTable from "../list/v-primary-table";
import vTakingMedicineTable from "../list/v-taking-medicine-table";
import vComplaintTable from "../list/v-complaint-table";
import vBloodTable from "../list/v-blood-table.vue";
import vOtherTable from "../list/v-other-table";
import vInitialQuestionTable from "../list/v-initial-question-table";
import vAlertBox from "../commons/v-alert-box"

import Helper from "../commons/functions.js"

export default {
  data: function() {
    return {
      patient: this.$route.params.patient,
      panel: [0],
      ranges: '',
    };
  },
  mounted: function(){
    this.initialize()
  },
  methods: {
    async initialize() {
      this.ranges = (await Api.get("/getaccetableintervals")).data
    },
    btnDelete: function() {
      let patient = this.patient;
      let router = this.$router;
      let mBox = this.$refs['message'];
      confirm("Do you want to delete patient " + 
      this.patient.last_name + " " + this.patient.first_name[0] + "." + 
      this.patient.middle_name[0] + ".") && Api
        .delete("/patient_request", {
          data: { patient }
        })
        .then(function(response) {
          console.log(response);
          router.go(-1);
        })
        .catch(function(e) {
          mBox.showMessage("Error", e, "error");
        });
    },
    btnSave: function() {
      let patient = this.patient;
      //let self = this;

      Api
        .put("/patient_request", {
          patient
        })
        .then(function(response) {
          console.log(response);
          //self.aBox.showMessage("Saved");
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    check_acceptability: function(name, instance){
      return Helper.check_acceptability(name, instance, this.ranges)
    }
  },
  components: {
    vPatient,
    vMessageBox,
    vPrimaryTable,
    vTakingMedicineTable,
    vComplaintTable,
    vBloodTable,
    vOtherTable,
    vAlertBox,
    vInitialQuestionTable
  }
};
</script>

<style>
</style>