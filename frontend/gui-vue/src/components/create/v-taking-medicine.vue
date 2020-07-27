<template>
<div >
  <v-row>
    <v-col cols="10" md="3">
      <v-date-custom
        label="From date of taking medicine"
        :date="takingmedicine_edit.fromdate"
        :change="fromdateChange"
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
      <v-date-custom label="Date" :date="takingmedicine_edit.date" :change="dateChange" />
    </v-col>
  </v-row>
  </div>
</template>

<script>
import vDateCustom from "../inputs/v-date-custom";
import Helper from "../commons/functions.js";

export default {
  name: "v-taking-medicine",
  components: {
    vDateCustom
  },
  props: ["takingmedicine"],
  data: function() {
    return {
      takingmedicine_edit: {
        fromdate: {
          value: this.takingmedicine.fromdate
        },
        date: {
          value: this.takingmedicine.date
        }
      }
    };
  },
  methods: {
    initialize() {
      if (typeof this.takingmedicine.id == "undefined") {
        this.takingmedicine_edit.date.value = Helper.GetCurrentDate();
        this.takingmedicine_edit.fromdate.value = Helper.GetCurrentDate();
      }
    },
    fromdateChange() {
      this.takingmedicine.fromdate = this.takingmedicine_edit.fromdate.value;
    },
    dateChange() {
      this.takingmedicine.date = this.takingmedicine_edit.date.value;
    }
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style>
</style>