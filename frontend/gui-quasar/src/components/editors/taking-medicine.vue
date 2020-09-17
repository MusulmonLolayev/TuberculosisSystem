<template>
<q-form ref="form">
<div>
  <div class="row">
    <div class="col-5">
      <q-input
        :label="$t('from_date_of_taking_medicine')"
        v-model="takingmedicine.fromdate"
        type='date'
      />
    </div>
    <div class="col-5">
      <q-checkbox v-model="takingmedicine.streptomycin" :label="$t('streptomycin')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="takingmedicine.rifampicin" :label="$t('rifampicin')" />
    </div>

    <div class="col-5">
      <q-checkbox v-model="takingmedicine.isoniazid" :label="$t('isoniazid')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="takingmedicine.pyrazinamide" :label="$t('pyrazinamide')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="takingmedicine.ethambutol" :label="$t('ethambutol')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="takingmedicine.status" :label="$t('status')" />
    </div>
    <div class="col-5">
      <q-input
        :label="$t('date')"
        v-model="takingmedicine.date"
        type='date'
      />
    </div>
  </div>
  </div>
</q-form>
</template>

<script>

export default {
  name: "TakingMedicine",
  props: ["takingmedicine"],
  methods: {
    initialize() {
      if (typeof this.takingmedicine.id == "undefined") {
        this.takingmedicine.date = this.$helper.GetCurrentDate();
        this.takingmedicine.fromdate = this.$helper.GetCurrentDate();
      }
    },
    hasError(){
      return this.$refs['form'].validate()
    }
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style>
</style>