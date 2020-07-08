<template>
    <div>
    <v-expansion-panels
      v-model="panel"
      focusable
      multiple
    >
    <v-snackbar
      :timeout="2000"
      :value="show_message"
      absolute
      top
      :color="message_type"
      outlined
      right
    >
      {{message}}
    </v-snackbar>
      <v-expansion-panel expanded>
        <v-expansion-panel-header><h2>General information</h2></v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-container>
            <v-row>
              <v-col>
                Full name: {{patient.last_name + " " + patient.first_name + " " + patient.middle_name}}
              </v-col>
              <v-col>
                Application number: {{patient.number}}
              </v-col>
              <v-col>  
                Data of birthday: {{patient.birthday}}
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                Sickness from: {{patient.fromdate}}
              </v-col>
              <v-col>  
                Sex: {{patient.gender ? 'Male' : 'Female'}}
              </v-col>
              <v-col>  
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

                <v-dialog
                  v-model="edit_dialog"
                  width="500"
                >
                  <v-card>
                    <PatientCard :patient="patient"/>
                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        text
                        @click="edit_dialog_Ok"
                      >
                        Close
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>                
              </v-col>
            </v-row>
          </v-container>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Primary diagonose</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          Some content
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Panel 3</v-expansion-panel-header>
        <v-expansion-panel-content>
          Some content
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import PatientCard from '../create/patient'
import Api from '@/api/Api'

export default {

    data: function(){
        return {
            patient: this.$route.params.patient,
            edit_dialog: false,
            panel: [0],
            show_message: false,
            message_type: 'success',
            message: '',
        }
    },
    mounted: function(){
      if (typeof this.patient.id != 'undefined'){
            this.GET_DISTRICT_FROM_API(this.patient.district)
        }
    },
    computed: {
      ...mapGetters([
            'DISTRICT',
        ]),
    },
    methods: {
      ...mapActions([
            'GET_DISTRICT_FROM_API',
        ]),
        btnDelete: function(){
            let patient = this.patient
            let router = this.$router
            Api().delete('/patientdelete', {
                data: patient,
            })
            .then(function(response){
                console.log(response)
                router.push('/data')
            })
            .catch(function(error){
                console.log(error)
            });
        },
        btnEdit: function(){
          this.edit_dialog = true
          //console.log('Edit')
        },
        edit_dialog_Ok: function(){
          this.edit_dialog = false
        },
        btnSave: function(){
            let patient = this.patient
            let self = this

            Api().post('/patientedit', {
                patient,
            })
            .then(function(response){
                console.log(response)
                self.showMessage('Success', 'success')
            })
            .catch(function(error){
                console.log(error)
            });
        },
        sleep: function(ms){
          return new Promise(resolve => setTimeout(resolve, ms));
        },
        showMessage: function(message, message_type){
          //console.log('dddd')
          this.message = message
          this.message_type = message_type
          this.show_message = true;
        }
    },
    components: {
        PatientCard
    }
}
</script>

<style>

</style>