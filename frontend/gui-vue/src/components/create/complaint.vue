<template>
  <v-container>
    <v-row>
      <v-col cols='10' md='3'>
        <v-checkbox
          v-model="complaint.diarrhea"
          label="Diarrhea"
        />
      </v-col>
      <v-col cols='10' md='3'>
        <v-checkbox
          v-model="complaint.pyrazinamide"
          label="Pyrazinamide"
        />
      </v-col>
      <v-col cols='10' md='3'>
        <v-checkbox
          v-model="complaint.ethambutol"
          label="Ethambutol"
        />
      </v-col>
      <v-col cols='10' md='3'>
        <v-checkbox
          v-model="complaint.flatulence"
          label="Flatulence"
        />
      </v-col>
      <v-col cols='10' md='3'>
        <v-checkbox
          v-model="complaint.stomachache"
          label="Stomachache"
        />
      </v-col>
      <v-col cols='10' md='3'>
        Stool frequency: 
        <v-text-field v-model="complaint.from_stool_frequency" label='from'/>
        <v-text-field v-model="complaint.to_stool_frequency" label='to'/>
      </v-col>
      <v-col cols="10" md="3">
        <v-select
          label="Character" 
          :items="characters"
          item-text='name'
          return-object
          item-value="id"
          @change="characterChanged"
          v-model="selectedcharacter" />
        </v-col>
    </v-row>
  </v-container>
</template>

<script>

import Api from '@/api/Api'

export default {
    name: 'Complaint',
    props: ['complaint'],
    data: function(){
      return{
        characters: [],
        selectedcharacter: {}
      }
    },

    methods: {
      characterChanged(e){
        this.complaint.character = e.id
      },
      GET_CHARACTERS_FROM_API(){
        let self = this
        Api().get('/characterofstool')
        .then((response) => {
          self.characters = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    mounted: function(){
      this.GET_CHARACTERS_FROM_API()
    }
}
</script>

<style>

</style>