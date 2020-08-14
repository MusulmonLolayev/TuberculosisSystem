<template>
  <v-row>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.diarrhea" label="Diarrhea" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.normal_stool" label="Normal stool" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.constipation" label="Constipation" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.flatulence" label="Flatulence" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.stomachache" label="Stomachache" />
    </v-col>
    <v-col cols="10" md="3">
      Stool frequency:
      <v-text-field v-model="complaint.from_stool_frequency" label="from" type="number" />
      <v-text-field v-model="complaint.to_stool_frequency" label="to" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-select
        label="Character"
        :items="CHARACTER_STOOLS"
        item-text="name"
        item-value="id"
        return-object
        v-model="selectedcharacter_stool"
        @change="changedCharacet_stool"
      />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="complaint.status" label="Status" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field
        label="Date of application"
        v-model="complaint.date"
        type='date'
      />
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Helper from "../commons/functions.js";

export default {
  name: "v-complaint",
  props: ["complaint"],
  data: function(){
    return {
      selectedcharacter_stool: 0
    }
  },
  computed: {
    ...mapGetters(["CHARACTER_STOOLS"])
  },
  methods: {
    ...mapActions(["GET_CHARACTER_STOOL_FROM_API"]),
    async initialize() {
      await this.GET_CHARACTER_STOOL_FROM_API()

      if (typeof this.complaint.id == "undefined"){
        this.complaint.date = Helper.GetCurrentDate();
        this.complaint.from_stool_frequency = 0
        this.complaint.to_stool_frequency = 0
        this.selectedcharacter_stool  = this.CHARACTER_STOOLS[0].id
      }
      else{
        this.selectedcharacter_stool = this.complaint.id
      }
    },
    changedCharacet_stool(id){
      this.complaint.changedCharacet_stool = id
    }
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style>
</style>