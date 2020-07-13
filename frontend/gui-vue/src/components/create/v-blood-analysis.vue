<template>
  <v-container>
    <v-row>
      <v-col cols="10" md="3">
        <v-text-field label="er" v-model="bloodanalysis.er" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="leyk" v-model="bloodanalysis.leyk" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="hb" v-model="bloodanalysis.hb" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="color" v-model="bloodanalysis.color" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="pok" v-model="bloodanalysis.pok" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="pya" v-model="bloodanalysis.pya" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="sya" v-model="bloodanalysis.sya" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="eoz" v-model="bloodanalysis.eoz" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="lf" v-model="bloodanalysis.lf" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="mon" v-model="bloodanalysis.mon" type="number" />
      </v-col>
      <v-col cols="10" md="3">
        <v-text-field label="coe" v-model="bloodanalysis.coe" type="number" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="bloodanalysis.status" label="Status" />
      </v-col>
      <v-col cols="10" md="4">
        <v-date-custom :date="editItem.date" :change="dateChange" label="Date" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import vDateCustom from '../inputs/v-date-custom'

export default {
  name: "v-blood-analysis",
  props: ["bloodanalysis"],
  data: function() {
    return {
      editItem: {
        date: {
          value: this.bloodanalysis.date
        }
      }
    };
  },
  methods: {
    dateChange() {
      this.bloodanalysis.date = this.editItem.date.value;
    }
  },
  components: {
      vDateCustom
  }
};
</script>

<style>
</style>