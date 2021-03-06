<template>
  <v-row ref="form">
    <v-col cols="10" md="3">
      <v-text-field
      ref="last_name" 
      label="Last name" 
      v-model="patient.last_name" 
      required clearable
      :rules="rules.name"
      />
    </v-col>

    <v-col cols="10" md="3">
      <v-text-field 
        ref="first_name" 
        label="First name" 
        v-model="patient.first_name" 
        required clearable
        :rules="rules.name"
        />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field
      ref="middle_name"  
      label="Middle name" 
      v-model="patient.middle_name" 
      required clearable
      :rules="rules.name"
      />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field
        label="Date of birthday"
        v-model="patient.birthday"
        type='date'
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
        :rules="rules.select"
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
      <v-text-field
      ref="address"  
      label="Address line" 
      required clearable
      v-model="patient.address" 
      :rules="rules.address"
      />
    </v-col>
    <v-col cols="10" md="3">
      <v-text-field
        label="Date of application"
        v-model="patient.fromdate"
        type='date'
      />
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
      <v-text-field 
      label="Number" 
      required 
      v-model="patient.number" 
      type='number'
      ref="number"
      :rules="rules.number" 
      />
    </v-col>
  </v-row>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Helper from "../commons/functions.js"

export default {
  name: "v-patient",
  props: ["patient"],
  data: function() {
    return {
      rules: {
        name : [
          value => !!value || 'Required.',
          value => (value && value.length >= 3) || 'Min 3 characters',
          value => /^[\w'][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*,.(){}|~<>;:[\]]{2,}$/.test(value) || 'Must be characters',
        ],
        address: [
          value => !!value || 'Required.',
          value => (value && value.length >= 3) || 'Min 3 characters',
        ],
        select: [
          value => !!value || 'Required.',
        ]
      },
      selectedCountry: {},
      selectedReigion: {},
      selectedDistrict: {},
      selectedOccupation: {},
      gender: 0,
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

        this.patient.birthday = Helper.GetCurrentDate()
        this.patient.fromdate = Helper.GetCurrentDate()
        this.patient.number = 1

        this.selectedOccupation = this.OCCUPATIONS[0].id
        this.patient.occupation = this.selectedOccupation

        this.selectedCountry = this.COUNTRIES[0].id
        await this.countryChanged(this.COUNTRIES[0])

        this.selectedReigion = this.REGIONS[0].id;
        await this.regionChanged(this.REGIONS[0]);
        
        this.selectedDistrict = this.DISTRICTS[0].id
        this.patient.district = this.selectedDistrict

      }
    },
    ...mapActions([
      "GET_COUNTRIES_FROM_API",
      "GET_REGIONS_FROM_API",
      "GET_DISTRICTS_FROM_API",
      "GET_OCCUPATIONS_FROM_API",
      "GET_DISTRICT_FROM_API"
    ]),   
    async countryChanged(e) {
      var url = "/regions_by_country/" + e.id;
      await this.GET_REGIONS_FROM_API(url);
    },
    async regionChanged(e) {
      var url = "/districts_by_region/" + e.id;
      await this.GET_DISTRICTS_FROM_API(url);
    },
    districtChanged(e) {
      this.patient.district = e.id;
    },
    occupationChanged(e) {
      this.patient.occupation = e.id;
    },
    rbChange(e) {
      this.patient.gender = e == 0 ? true : false;
    },
    hasError(){
      let res = false;
      ['last_name', 'first_name', 
      'middle_name', 'address'].forEach(f => {
        if (typeof this.$refs[f] != 'undefined' && this.$refs[f].hasError){
            this.$refs[f].validate(true)
            res = true
        }          
      }) 
      return res
    }
  },
  beforeMount: function() {
    this.initialize();
  },
  watch: {

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