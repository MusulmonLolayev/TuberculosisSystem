<template>
  <q-form ref="form">
    <div class="row">
      <div class="col-5">
        <q-checkbox v-model="other.tuberculosis_tolerance" :label="$t('tolerance')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.related_disease" :label="$t('related_disease')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.nausea" :label="$t('nausea')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.vomiting" :label="$t('vomiting')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.headache" :label="$t('headache')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.sweating" :label="$t('sweating')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.weakness" :label="$t('weakness')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.allergodermatosis" :label="$t('allergodermatosis')" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.coproscopy" :label="$t('coproscopy')" />
      </div>
      <div class="col-5">
        Weight loss:
        <q-input v-model="other.from_weight_loss" :label="$t('from')" type="number" />
        <q-input v-model="other.to_weight_loss" :label="$t('to')" type="number" />
      </div>
      <div class="col-5">
        <q-checkbox v-model="other.status" :label="$t('status')" />
      </div>
      <div class="col-5">
        <q-input
          :label="$t('date')"
          v-model="other.date"
          type='date'
        />
      </div>
    </div>
  </q-form>
</template>
<script>
export default {
  name: "Other",
  props: ["other"],
  methods: {
    initialize() {
      if (typeof this.other.id == "undefined") {
        
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