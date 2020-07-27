<template>
  <v-row>
    <v-col cols="10" md="3">
      <v-text-field label="Last name" v-model="patient.last_name" required />
    </v-col>

    <v-col cols="10" md="3">
      <v-text-field label="First name" v-model="patient.first_name" required />
    </v-col>

    <v-col cols="10" md="3">
      <v-text-field label="Middle name" v-model="patient.middle_name" required />
    </v-col>
    <v-col cols="10" md="3">
      <v-date-custom
        label="Date of birthday"
        :date="patient_edit.birthday"
        :change="birthdayChange"
      />
    </v-col>

    <v-col cols="10" md="3">
      <v-radio-group row v-model="gender" @change="rbChange">
        <v-radio label="Male" :value="0" />
        <v-radio label="Female" :value="1" />
      </v-radio-group>
    </v-col>
    <v-col cols="10" md="3">
      <v-select
        label="Country"
        :items="COUNTRIES"
        item-text="name"
        @change="countryChanged"
        return-object
        item-value="id"
        v-model="selectedCountry"
      />
    </v-col>

    <v-col cols="10" md="3">
      <v-select
        label="Region"
        :items="REGIONS"
        item-text="name"
        @change="regionChanged"
        return-object
        item-value="id"
        v-model="selectedReigion"
      />
    </v-col>
    <v-col cols="10" md="3">
      <v-select
        label="District"
        :items="DISTRICTS"
        item-text="name"
        return-object
        item-value="id"
        v-model="selectedDistrict"
        @change="districtChanged"
      />
    </v-col>

    <v-col cols="10" md="6">
      <v-text-field label="Address line" required v-model="patient.address" />
    </v-col>
    <v-col cols="10" md="3">
      <v-date-custom label="From date" :date="patient_edit.fromdate" :change="fromdateChange" />
    </v-col>

    <v-col cols="10" md="3">
      <v-select
        label="Occupation"
        :items="OCCUPATIONS"
        item-text="title"
        return-object
        item-value="id"
        @change="occupationChanged"
        v-model="selectedOccupation"
      />
    </v-col>

    <v-col cols="10" md="3">
      <v-text-field label="Number" required v-model="patient.number" type='number'/>
    </v-col>
  </v-row>
</template>

<script>
import vDateCustom from "../inputs/v-date-custom";
import { mapActions, mapGetters } from "vuex";
import Helper from "../commons/functions.js"

export default {
  name: "v-patient",
  components: {
    vDateCustom
  },
  props: ["patient"],
  data: function() {
    return {
      patient_edit: {
        birthday: {
          value: this.patient.birthday
        },
        fromdate: {
          value: this.patient.fromdate
        }
      },
      selectedCountry: {},
      selectedReigion: {},
      selectedDistrict: {},
      selectedOccupation: {},
      gender: 0
    };
  },
  computed: {
    ...mapGetters([
      "COUNTRIES",
      "REGIONS",
      "DISTRICTS",
      "OCCUPATIONS",
      "DISTRICT"
    ])
  },
  methods: {
    async initialize() {
      await this.GET_COUNTRIES_FROM_API();
      await this.GET_OCCUPATIONS_FROM_API();

      if (typeof this.patient.id != "undefined") {
        await this.GET_DISTRICT_FROM_API(this.patient.district);

        // select region, country and district by patient for editing
        this.selectedCountry = this.DISTRICT.region.country.id;
        // when the country changes then must notice about it by calling the method.
        await this.countryChanged(this.DISTRICT.region.country);

        this.selectedReigion = this.DISTRICT.region.id;
        // it is as same as the country selection
        await this.regionChanged(this.DISTRICT.region);

        this.selectedDistrict = this.DISTRICT.id;

        // set gender
        this.gender = this.patient.gender == true ? 0 : 1;

        // set occupation
        this.selectedOccupation = this.patient.occupation;
      }
      else {
        // overwise set defualt values on patient
        this.patient_edit.birthday.value = Helper.GetCurrentDate()
        this.patient_edit.fromdate.value = Helper.GetCurrentDate()
        
        /*this.selectedCountry = this.COUNTRIES[0].id
        await this.countryChanged(this.COUNTRIES[0])

        this.selectedReigion = this.REGIONS[0].id;
        await this.regionChanged(this.REGIONS[0]);
        
        this.selectedDistrict = this.DISTRICT.id*/
      }
    },
    ...mapActions([
      "GET_COUNTRIES_FROM_API",
      "GET_REGIONS_FROM_API",
      "GET_DISTRICTS_FROM_API",
      "GET_OCCUPATIONS_FROM_API",
      "GET_DISTRICT_FROM_API"
    ]),

    countryChanged(e) {
      var url = "/regions_by_country/" + e.id;
      this.GET_REGIONS_FROM_API(url);
    },
    regionChanged(e) {
      var url = "/districts_by_region/" + e.id;
      this.GET_DISTRICTS_FROM_API(url);
    },
    districtChanged(e) {
      this.patient.district = e.id;
    },
    occupationChanged(e) {
      this.patient.occupation = e.id;
    },
    birthdayChange() {
      this.patient.birthday = this.patient_edit.birthday.value;
    },
    fromdateChange() {
      this.patient.fromdate = this.patient_edit.fromdate.value;
    },
    rbChange(e) {
      this.patient.gender = e == 0 ? true : false;
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>

<style scoped>
.card-form {
  margin: auto;
  margin-top: 50px;
  max-width: 850px;
  width: 100%;
  border-radius: 10px;
  padding: 10px;
  float: center;
}
.header {
  align-content: center;
}
label {
  margin: 10px;
  margin-inline: initial;
}
</style>