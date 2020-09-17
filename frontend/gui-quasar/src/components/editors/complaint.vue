<template>
<q-form ref="form">
  <div class="row">
    <div class="col-5">
      <q-checkbox v-model="complaint.diarrhea" :label="$t('diarrhea')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="complaint.normal_stool" :label="$t('normal_stool')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="complaint.constipation" :label="$t('constipation')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="complaint.flatulence" :label="$t('flatulence')" />
    </div>
    <div class="col-5">
      <q-checkbox v-model="complaint.stomachache" :label="$t('stomachache')" />
    </div>
    <div class="col-5">
      {{$t('stool_frequency')}}:
      <q-input v-model="complaint.from_stool_frequency" :label="$t('from')" type="number" />
      <q-input v-model="complaint.to_stool_frequency" :label="$t('to')" type="number" />
    </div>
    <div class="col-5">
      <q-select
        v-model="complaint.character"
        :label="$t('character')"
        :options="character_stools"
        map-options
        emit-value
        option-value="id"
        option-label="name"
      />
    </div>
    <div class="col-5">
      <q-checkbox v-model="complaint.status" :label="$t('status')" />
    </div>
    <div class="col-5">
      <q-input
        :label="$t('date')"
        v-model="complaint.date"
        type='date'
      />
    </div>
  </div>
</q-form>
</template>

<script>
export default {
  name: "Complaint",
  props: ["complaint"],
  data: function(){
      return {
          character_stools: [],
      }
  },
  methods: {
    async initialize() {
      let response = await this.$axios.get('/characterofstool')
        this.character_stools = response.data
      if (typeof this.complaint.id == "undefined"){
        this.complaint.date = this.$helper.GetCurrentDate();
        this.complaint.from_stool_frequency = 0
        this.complaint.to_stool_frequency = 0
        this.complaint.character = this.character_stools[0].id
      }
      else{
        //this.selectedcharacter_stool = this.complaint.character
      }
    },
    hasError(){
      return this.$refs['form'].validate()
    }
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style>
</style>