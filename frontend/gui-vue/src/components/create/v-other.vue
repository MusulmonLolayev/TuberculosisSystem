<template>
  <v-container>
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
      <v-col cols="10" md="3">
        <v-checkbox v-model="other.allergodermatosis" label="Allergodermatosis" />
      </v-col>
      <v-col cols="10" md="2">
        <v-checkbox v-model="other.coproscopy" label="Coproscopy" />
      </v-col>
      <v-col cols="10" md="3">
        Weight loss:
        <v-text-field v-model="other.from_weight_loss" label="from" type="number" />
        <v-text-field v-model="other.to_weight_loss" label="to" type="number" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="other.status" label="Status" />
      </v-col>
      <v-col cols="10" md="3">
        <v-date-custom label="Date" :date="editItem.date" :change="dateChange" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import vDateCustom from '../inputs/v-date-custom'

export default {
  name: "v-other",
  props: ["other"],
  data: function() {
    return {
      editItem: {
        date: {
          value: this.other.date
        }
      }
    };
  },
  methods: {
    dateChange() {
      this.other.date = this.editItem.date.value;
    }
  },
  components: {
    vDateCustom
  }
};
</script>

<style>
</style>