<template>
  <div>
    <v-row>
      <v-col cols="10" md="3">
        <v-select
          label="Clinical form of Tuberculosis"
          :items="CLINICAL_FORMS"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.clinicalform"
        />
      </v-col>
      <v-col cols="10" md="3">
        <v-select
          label="Localization"
          :items="LOCALIZATIONS"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.localization"
        />
      </v-col>
      <v-col cols="10" md="3">
        <v-select
          label="Prevalence"
          :items="PREVALENCES"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.prevalence"
        />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.infiltration" label="Infiltration" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.decay" label="Decay" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.seeding" label="Seeding" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.resorption" label="Resorption" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.compaction" label="Compaction" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.scarring" label="Scarring" />
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.calcification" label="Calcification" />
      </v-col>
      <v-col cols="10" md="3">
        BK
        <v-radio-group row v-model="primarydiagnose.bk">
          <v-radio label="+" :value="true" />
          <v-radio label="-" :value="false" />
        </v-radio-group>
      </v-col>
      <v-col cols="10" md="3">
        <v-checkbox v-model="primarydiagnose.status" label="Status" />
      </v-col>

      <v-col cols="10" md="3">
        <v-text-field
        label="Date"
        v-model="primarydiagnose.date"
        type='date'
      />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Helper from "../commons/functions.js";

export default {
  name: "v-primary-diagnose",
  props: ["primarydiagnose"],
  methods: {
    async initialize() {
      Promise.all([
        this.GET_CLINICAL_FORMS_FROM_API(),
        this.GET_LOCALIZATION_FROM_API(),
        this.GET_PREVALENCES_FROM_API()
      ]);
      if (typeof this.primarydiagnose.id == 'undefined'){
        
        this.primarydiagnose.date =  Helper.GetCurrentDate()

        /*// then default vaules to primary diagnose
        this.primarydiagnose.clinicalform = this.CLINICAL_FORMS[0].id
        this.primarydiagnose.localization = this.LOCALIZATIONS[0].id
        this.primarydiagnose.prevalence = this.PREVALENCES[0].id*/
      }
    },
    ...mapActions([
      "GET_CLINICAL_FORMS_FROM_API",
      "GET_LOCALIZATION_FROM_API",
      "GET_PREVALENCES_FROM_API"
    ]),
  },
  computed: {
    ...mapGetters(["CLINICAL_FORMS", "LOCALIZATIONS", "PREVALENCES"])
  },
  beforeMount: function() {
    this.initialize();
  },
};
</script>

<style>
</style>