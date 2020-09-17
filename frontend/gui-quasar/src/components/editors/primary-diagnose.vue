<template>
  <q-form ref='form'>
  <div>
    <div class="row">
      <div class="col-5">
        <q-select
          :label="$t('clinical_form_of_tuberculosis')"
          :options="clinicalforms"
          option-value="id"
          option-label="name"
          emit-value
          map-options
          v-model="primarydiagnose.clinicalform"
          :rules="$helper.rules.select"
        />
      </div>
      <div class="col-5">
        <q-select
          :label="$t('localization')"
          :options="localizations"
          option-value="id"
            option-label="name"
            emit-value
            map-options
          v-model="primarydiagnose.localization"
          :rules="$helper.rules.select"
        />
      </div>
      <div class="col-5">
        <q-select
          :label="$t('prevalence')"
          :options="prevalences"
          option-value="id"
            option-label="name"
            emit-value
            map-options
          v-model="primarydiagnose.prevalence"
          :rules="$helper.rules.select"
        />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.infiltration" :label="$t('infiltration')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.decay" :label="$t('decay')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.seeding" :label="$t('seeding')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.resorption" :label="$t('resorption')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.compaction" :label="$t('compaction')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.scarring" :label="$t('scarring')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.calcification" :label="$t('calcification')" />
      </div>
      <div class="col-5">
        BK: 
          <q-radio v-model="primarydiagnose.bk" label="+" :val="true" />
          <q-radio v-model="primarydiagnose.bk" label="-" :val="false" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="primarydiagnose.status" :label="$t('status')" />
      </div>

      <div class="col-5">
        <q-input
        :label="$t('date')"
        v-model="primarydiagnose.date"
        type='date'
      />
      </div>
    </div>
  </div>
  </q-form>
</template>

<script>
export default {
  name: "PrimaryDiagnose",
  props: ["primarydiagnose"],
  data: function(){
    return{
      selectedClinicalform: '',
      selectedLocalization: '',
      selectedPrevalence: '',
      clinicalforms: [],
      localizations: [],
      prevalences: [],
    }
  },
  methods: {
    async initialize() {

        let response = await this.$axios.get('/clinicalforms')
        this.clinicalforms = response.data
        
        response = await this.$axios.get('/localization')
        this.localizations = response.data

        response = await this.$axios.get('/prevalence')
        this.prevalences = response.data

      if (typeof this.primarydiagnose.id == 'undefined'){
        this.primarydiagnose.date =  this.$helper.GetCurrentDate()

        // then default vaules to primary diagnose
        this.primarydiagnose.clinicalform  = this.clinicalforms[0].id
        this.primarydiagnose.localization = this.localizations[0].id
        this.primarydiagnose.prevalence = this.prevalences[0].id
      }
      else{
        // then default vaules to primary diagnose
      }
    },
    hasError(){
      return this.$refs.form.validate()
    },
  },
  beforeMount: function() {
    this.initialize();
  },
};
</script>

<style scop>
    div.col-5 {
        margin-left: 5px;
        margin-right: 5px;
    }
</style>