<template>
  <v-row>
    <v-col cols="10" md="2">
      <v-text-field label="er" v-model="bloodanalysis.er" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="leyk" v-model="bloodanalysis.leyk" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="hb" v-model="bloodanalysis.hb" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="color" v-model="bloodanalysis.color" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="pya" v-model="bloodanalysis.pya" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="sya" v-model="bloodanalysis.sya" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="eoz" v-model="bloodanalysis.eoz" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="lf" v-model="bloodanalysis.lf" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="mon" v-model="bloodanalysis.mon" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-text-field label="coe" v-model="bloodanalysis.coe" type="number" />
    </v-col>
    <v-col cols="10" md="2">
      <v-checkbox v-model="bloodanalysis.status" label="Status" />
    </v-col>
    <v-col cols="10" md="2">
      <v-date-custom :date="editItem.date" :change="dateChange" label="Date" />
    </v-col>
  </v-row>
</template>

<script>
import vDateCustom from "../inputs/v-date-custom";

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
    initialize() {
      if (typeof this.bloodanalysis.id == "undefined") {
        this.bloodanalysis.er = 0;
        this.bloodanalysis.leyk = 0;
        this.bloodanalysis.hb = 0;
        this.bloodanalysis.color = 0;
        this.bloodanalysis.pya = 0;
        this.bloodanalysis.sya = 0;
        this.bloodanalysis.eoz = 0;
        this.bloodanalysis.lf = 0;
        this.bloodanalysis.mon = 0;
        this.bloodanalysis.hb = 0;
        this.bloodanalysis.coe = 0;
      }
    },
    dateChange() {
      this.bloodanalysis.date = this.editItem.date.value;
    }
  },
  created() {
    this.initialize();
  },
  components: {
    vDateCustom
  }
};
</script>

<style>
</style>