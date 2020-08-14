<template>
  <div>
    <v-row>
      <v-col cols="10" md="3">
        <v-select
          label="Clinical form of Tuberculosis"
          :items="CLINICAL_FORMS"
          item-text="name"
          item-value="id"
          return-object
          v-model="selectedClinicalform"
          @change="clinicalChanged"
        />
      </v-col>
      <v-col cols="10" md="3">
        <v-select
          label="Localization"
          :items="LOCALIZATIONS"
          item-text="name"
          item-value="id"
          v-model="selectedLocalization"
          @change="localizationChanged"
          return-object
        />
      </v-col>
      <v-col cols="10" md="3">
        <v-select
          label="Prevalence"
          :items="PREVALENCES"
          item-text="name"
          item-value="id"
          v-model="selectedPrevalence"
          @change="prevalenceChanged"
          return-object
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
  data: function(){
    return{
      selectedClinicalform: '',
      selectedLocalization: '',
      selectedPrevalence: '',
    }
  },
  methods: {
    async initialize() {
      await this.GET_CLINICAL_FORMS_FROM_API()
      await this.GET_LOCALIZATION_FROM_API()
      await this.GET_PREVALENCES_FROM_API()

      if (typeof this.primarydiagnose.id == 'undefined'){
        this.primarydiagnose.date =  Helper.GetCurrentDate()

        // then default vaules to primary diagnose
        this.selectedClinicalform = this.CLINICAL_FORMS[0].id
        this.selectedLocalization = this.LOCALIZATIONS[0].id
        this.selectedPrevalence = this.PREVALENCES[0].id
      }
      else{
        // then default vaules to primary diagnose
        this.selectedClinicalform = this.primarydiagnose.clinicalform
        this.selectedLocalization = this.primarydiagnose.localization
        this.selectedPrevalence = this.primarydiagnose.prevalence
      }
    },
    clinicalChanged(id){
      this.primarydiagnose.clinicalform = id
    },
    localizationChanged(id){
      this.primarydiagnose.localization = id
    },
    prevalenceChanged(id){
      this.primarydiagnose.prevalence = id
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