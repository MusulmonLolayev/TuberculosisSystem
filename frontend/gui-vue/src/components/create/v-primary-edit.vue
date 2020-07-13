<template>
  <v-container>
    <v-row>
      <v-col cols="10" md="4">
        <v-select
          label="Clinical form of Tuberculosis"
          :items="CLINICAL_FORMS"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.clinicalform"
        />
      </v-col>
      <v-col cols="10" md="4">
        <v-select
          label="Localization"
          :items="LOCALIZATIONS"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.localization"
        />
      </v-col>
      <v-col cols="10" md="4">
        <v-select
          label="Prevalence"
          :items="PREVALENCES"
          item-text="name"
          item-value="id"
          v-model="primarydiagnose.prevalence"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.infiltration" label="Infiltration" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.decay" label="Decay" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.seeding" label="Seeding" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.resorption" label="Resorption" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.compaction" label="Compaction" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.scarring" label="Scarring" />
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.calcification" label="Calcification" />
      </v-col>
      <v-col cols="10" md="3">
        BK
        <v-radio-group row v-model="primarydiagnose.bk">
          <v-radio label="+" :value="true" />
          <v-radio label="-" :value="false" />
        </v-radio-group>
      </v-col>
      <v-col cols="10" md="4">
        <v-checkbox v-model="primarydiagnose.status" label="Status" />
      </v-col>

      <v-col cols="10" md="4">
        <v-date-custom :date="editItem.date" :change='dateChange' label="Date" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import vDateCustom from '../inputs/v-date-custom'

export default {
  name: "v-primary-edit",
  props: ["primarydiagnose"],
  data: function() {
    return {
      editItem: {
        date: {
          value: this.primarydiagnose.date
        }
      }
    };
  },
  methods: {
    ...mapActions([
      "GET_CLINICAL_FORMS_FROM_API",
      "GET_LOCALIZATION_FROM_API",
      "GET_PREVALENCES_FROM_API"
    ]),
    dateChange() {
      this.primarydiagnose.date = this.editItem.date.value;
    }
  },
  computed: {
    ...mapGetters(["CLINICAL_FORMS", "LOCALIZATIONS", "PREVALENCES"])
  },
  mounted() {
    this.GET_CLINICAL_FORMS_FROM_API();
    this.GET_LOCALIZATION_FROM_API();
    this.GET_PREVALENCES_FROM_API();
  },
  components: {
    vDateCustom
  }
};
</script>

<style>
</style>