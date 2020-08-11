<template>
<div >
  <v-row>
    <v-col cols="10" md="3">
      <v-text-field
        label="From date of taking medicine"
        v-model="takingmedicine.fromdate"
        type='date'
      />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.streptomycin" label="Streptomycin" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.rifampicin" label="Rifampicin" />
    </v-col>

    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.isoniazid" label="Isoniazid" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.pyrazinamide" label="Pyrazinamide" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.ethambutol" label="Ethambutol" />
    </v-col>
    <v-col cols="10" md="3">
      <v-checkbox v-model="takingmedicine.status" label="Status" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field
        label="Date"
        v-model="takingmedicine.date"
        type='date'
      />
    </v-col>
  </v-row>
  </div>
</template>

<script>
import Helper from "../commons/functions.js";

export default {
  name: "v-taking-medicine",
  props: ["takingmedicine"],
  methods: {
    initialize() {
      if (typeof this.takingmedicine.id == "undefined") {
        this.takingmedicine.date = Helper.GetCurrentDate();
        this.takingmedicine.fromdate = Helper.GetCurrentDate();
      }
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style>
</style>