<template>
    <div>
      <MessageBox :data='mBox'/>
    <v-expansion-panels
      v-model="panel"
      focusable
      multiple
      hover
      popout
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
      <v-expansion-panel>
        <v-expansion-panel-header><h2>General information</h2></v-expansion-panel-header>
        <v-expansion-panel-content>
            <v-row>
              <v-col cols='12' md='4'>
                Full name: {{patient.last_name + " " + patient.first_name + " " + patient.middle_name}}
              </v-col>
              <v-col  cols='12' md='4'>
                Application number: {{patient.number}}
              </v-col>
              <v-col  cols='12' md='4'>  
                Data of birthday: {{patient.birthday}}
              </v-col>
              <v-col  cols='12' md='4'>
                Sickness from: {{patient.fromdate}}
              </v-col>
              <v-col  cols='12' md='4'>  
                Sex: {{patient.gender ? 'Male' : 'Female'}}
              </v-col>
              <v-col  cols='12' md='4'>  
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
                  width="600"
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
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>
          <h2>Primary diagonose</h2>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-data-table
            :headers="headers_primary"
            :items="primaries"
            sort-by="calories"
            class="elevation-1">
            <template v-slot:top>
              <v-toolbar flat color="white">
                <v-toolbar-title>List of primary diagonoses</v-toolbar-title>
                <v-divider
                  class="mx-4"
                  inset
                  vertical
                ></v-divider>
                <v-spacer></v-spacer>
                <v-btn
                      color="primary"
                      dark
                      class="mb-2"
                      @click="primaryDialog = true"

                    >New Item</v-btn>
                <v-dialog v-model="primaryDialog" max-width="500px">
                  <v-card>
                    <v-card-text>
                      <PrimaryDiagnose :primarydiagnose='defaultPrimary'/>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                      <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-toolbar>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                small
                @click="deleteItem(item)"
              >
                mdi-delete
              </v-icon>
            </template>
            <template v-slot:no-data>
              <v-btn color="primary" @click="initialize">Reset</v-btn>
            </template>
          </v-data-table>
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
import MessageBox from '../commons/messagebox'
import MessgeBox_Class from '../commons/messagebox_class'
import PrimaryDiagnose from '../create/primarydiagnose'

export default {

    data: function(){
        return {
            patient: this.$route.params.patient,
            edit_dialog: false,
            panel: [0, 1],
            show_message: false,
            message_type: 'success',
            message: '',
            mBox: new MessgeBox_Class(),
            primaryDialog: false,
            headers_primary: [
              {
                text: 'Clinical form of disease',
                align: 'start',
                sortable: false,
                value: 'name',
              },
              { text: 'Localization', value: 'name', align: 'start', sortable: false},
              { text: 'Prevalence', value: 'name', align: 'start', sortable: false},
              { text: 'Infiltration', value: 'name', align: 'start', sortable: false},
              { text: 'Decay', value: 'name'},
              { text: 'Seeding', value: 'name'},
              { text: 'Resorption', value: 'name'},
              { text: 'Compaction', value: 'name'},
              { text: 'Scarring', value: 'name'},
              { text: 'Calcification', value: 'name'},
              { text: 'BK', value: 'name'},
              { text: 'Status', value: 'name'},
              { text: 'Actions', value: 'actions', sortable: false },
          ],
          primaries: [],
          editedIndex: -1,
          editedItem: {
            name: '',
            calories: 0,
            fat: 0,
            carbs: 0,
            protein: 0,
          },
          defaultPrimary: {
          },
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
            let mBox = this.mBox
            Api().delete('/patient_request',{
              data: {patient}
            })
            .then(function(response){
                console.log(response)
                router.go(-1)
            })
            .catch(function(e){
                mBox.showMessage('Error', e, 'error')
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

            Api().put('/patient_request', {
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
        PatientCard,
        MessageBox,
        PrimaryDiagnose
    }
}
</script>

<style>

</style>