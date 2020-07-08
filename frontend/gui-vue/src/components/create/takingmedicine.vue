<template>
  <v-container>
      <v-row>
          <v-col cols='10' md='3'>
            <datepicker 
                label='From date of taking medicine'
                :date="takingmedicine_edit.fromdate" 
                :change="fromdateChange"    
            />
          </v-col>
          <v-col cols="10" md="2">
            <v-checkbox
                v-model="takingmedicine.streptomycin"
                label="Streptomycin"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="takingmedicine.rifampicin"
                label="Rifampicin"
            />
         </v-col>

         <v-col cols="10" md="2">
            <v-checkbox
                v-model="takingmedicine.isoniazid"
                label="Isoniazid"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="takingmedicine.pyrazinamide"
                label="Pyrazinamide"
            />
         </v-col>
         <v-col cols="10" md="2">
            <v-checkbox
                v-model="takingmedicine.ethambutol"
                label="Ethambutol"
            />
         </v-col>
      </v-row>
  </v-container>
</template>

<script>

import datepicker from '../inputs/datepicker'

export default {
    name: 'TakingMedicine',
    components: {
        datepicker,
    },
    props: [
        'takingmedicine'
    ],
    data: function(){
        return {
            takingmedicine_edit: {
                fromdate: {
                    'value': this.takingmedicine.fromdate
                },
            }
        }
    },
    methods: {
        fromdateChange(){
            this.takingmedicine.fromdate = this.takingmedicine_edit.fromdate.value
        }
    },
}
</script>

<style>

</style>