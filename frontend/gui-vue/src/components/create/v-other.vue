<template>
  <v-row>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.tuberculosis_tolerance" label="Tuberculosis tolerance" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.related_disease" label="Related disease" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.nausea" label="Nausea" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.vomiting" label="Vomiting" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.headache" label="Headache" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.sweating" label="Sweating" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.weakness" label="Weakness" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.allergodermatosis" label="Allergodermatosis" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.coproscopy" label="Coproscopy" />
    </v-col>
    <v-col cols="10" md="2">
      Weight loss:
      <v-text-field v-model="other.from_weight_loss" label="from" type="number" />
      <v-text-field v-model="other.to_weight_loss" label="to" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="other.status" label="Status" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field
        label="Date"
        v-model="other.date"
        type='date'
      />
    </v-col>
  </v-row>
</template>

<script>
import Helper from "../commons/functions.js";

export default {
  name: "v-other",
  props: ["other"],
  methods: {
    initialize() {
      if (typeof this.other.id == "undefined") {
        this.other.date = Helper.GetCurrentDate();
        this.other.from_weight_loss = 0
        this.other.to_weight_loss = 0
      }
    },
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style>
</style>