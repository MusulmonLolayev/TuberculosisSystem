<template>
  <v-row>
    <v-col cols="10" md="3">
      <v-text-field label="CD3" v-model="immunogram.cd3" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="CD4" v-model="immunogram.cd4" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="CD8" v-model="immunogram.cd8" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="CD20" v-model="immunogram.cd20" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="IgM" v-model="immunogram.igm" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="IgG" v-model="immunogram.igg" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="IgA" v-model="immunogram.iga" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="TgE" v-model="immunogram.tge" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="ACT" v-model="immunogram.act" type="number" />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field label="ALT" v-model="immunogram.alt" type="number" />
    </v-col>

    <v-col cols="10" md="4">
      <v-checkbox v-model="immunogram.status" label="Status" />
    </v-col>
    <v-col cols="10" md="4">
      <v-date-custom :date="editItem.date" :change="dateChange" label="Date" />
    </v-col>
  </v-row>
</template>

<script>
import vDateCustom from "../inputs/v-date-custom";
import Helper from "../commons/functions.js";

export default {
  name: "v-immunogram",
  props: ["immunogram"],
  data: function() {
    return {
      editItem: {
        date: {
          value: this.immunogram.date
        }
      }
    };
  },
  methods: {
    initialize() {
      if (typeof this.immunogram.id == "undefined") {
        this.immunogram.cd3 = 0;
        this.immunogram.cd4 = 0;
        this.immunogram.cd8 = 0;
        this.immunogram.cd20 = 0;
        this.immunogram.igm = 0;
        this.immunogram.igg = 0;
        this.immunogram.iga = 0;
        this.immunogram.tge = 0;
        this.immunogram.act = 0;
        this.immunogram.alt = 0;
        this.editItem.date.value = Helper.GetCurrentDate();
      }
    },
    dateChange() {
      this.immunogram.date = this.editItem.date.value;
    }
  },
  mounted() {
    this.initialize();
  },
  components: {
    vDateCustom
  }
};
</script>

<style>
</style>