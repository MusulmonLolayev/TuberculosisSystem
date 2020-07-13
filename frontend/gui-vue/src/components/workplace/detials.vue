<template>
  <div>
    <v-message-box :data="mBox" />
    <v-expansion-panels v-model="panel" focusable multiple hover popout>
      <v-snackbar
        :timeout="2000"
        :value="show_message"
        absolute
        top
        :color="message_type"
        outlined
        right
      >{{message}}</v-snackbar>
      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>General information</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row>
            <v-col
              cols="12"
              md="4"
            >Full name: {{patient.last_name + " " + patient.first_name + " " + patient.middle_name}}</v-col>
            <v-col cols="12" md="4">Application number: {{patient.number}}</v-col>
            <v-col cols="12" md="4">Data of birthday: {{patient.birthday}}</v-col>
            <v-col cols="12" md="4">Sickness from: {{patient.fromdate}}</v-col>
            <v-col cols="12" md="4">Sex: {{patient.gender ? 'Male' : 'Female'}}</v-col>
            <v-col cols="12" md="4">
              Address: {{ DISTRICT.region.country.name + ", " +
              DISTRICT.region.name + ", " +
              DISTRICT.name + ", " +
              patient.address}}
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn text @click="btnDelete">Delete</v-btn>
              <v-btn text @click="btnEdit">Edit</v-btn>
              <v-btn text @click="btnSave">Save</v-btn>

              <v-dialog v-model="edit_dialog" width="600">
                <v-card>
                  <v-patient :patient="patient" />
                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="edit_dialog_Ok">Close</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-col>
          </v-row>
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
          <v-blood-table :patient="patient" />
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Immunogram</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-immunogram-table :patient="patient" />
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
import { mapActions, mapGetters } from "vuex";
import vPatient from "../create/v-patient";
import Api from "@/api/Api";
import vMessageBox from "../commons/v-message-box";
import MessageBox from "../commons/messagebox.js";
import vPrimaryTable from "../list/v-primary-table";
import vTakingMedicineTable from "../list/v-taking-medicine-table";
import vComplaintTable from '../list/v-complaint-table'
import vBloodTable from '../list/v-blood-table.vue'
import vImmunogramTable from '../list/v-immunogram-table'
import vOtherTable from '../list/v-other-table'

export default {
  data: function() {
    return {
      patient: this.$route.params.patient,
      edit_dialog: false,
      panel: [6],
      show_message: false,
      message_type: "success",
      message: "",
      mBox: new MessageBox(),
    };
  },
  mounted: function() {
    if (typeof this.patient.id != "undefined") {
      this.GET_DISTRICT_FROM_API(this.patient.district);
    }
  },
  computed: {
    ...mapGetters(["DISTRICT"])
  },
  methods: {
    ...mapActions(["GET_DISTRICT_FROM_API"]),
    btnDelete: function() {
      let patient = this.patient;
      let router = this.$router;
      let mBox = this.mBox;
      Api()
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
    btnEdit: function() {
      this.edit_dialog = true;
      //console.log('Edit')
    },
    edit_dialog_Ok: function() {
      this.edit_dialog = false;
    },
    btnSave: function() {
      let patient = this.patient;
      let self = this;

      Api()
        .put("/patient_request", {
          patient
        })
        .then(function(response) {
          console.log(response);
          self.showMessage("Success", "success");
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    sleep: function(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    showMessage: function(message, message_type) {
      //console.log('dddd')
      this.message = message;
      this.message_type = message_type;
      this.show_message = true;
    }
  },
  components: {
    vPatient,
    vMessageBox,
    vPrimaryTable,
    vTakingMedicineTable,
    vComplaintTable,
    vBloodTable,
    vImmunogramTable,
    vOtherTable
  }
};
</script>

<style>
</style>