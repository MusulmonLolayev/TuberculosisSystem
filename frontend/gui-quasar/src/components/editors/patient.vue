<template>
<q-form ref="form">
  <div class="row">
    <div class="input_div">
        <q-input
            :rules="rules.name"
            clearable
            v-model="patient.last_name"
            :label="$t('last_name')"
        />
    </div>
    <div class="input_div">
        <q-input
            :rules="rules.name"
            clearable
            v-model="patient.first_name"
            :label="$t('first_name')"
        />
    </div>
    <div class="input_div">
        <q-input
            :rules="rules.name"
            clearable
            v-model="patient.middle_name"
            :label="$t('middle_name')"
        />
    </div>
    <div class="input_div">
        <q-input
            clearable
            v-model="patient.birthday"
            :label="$t('birthday_date')"
            type='date'
        />
    </div>
    <div class="input_div">
        <q-radio v-model="patient.gender" :val="true" :label="$t('male')" />
        <q-radio v-model="patient.gender" :val="false" :label="$t('female')" />
    </div>

    <div class="input_div">
         <q-select
            :label="$t('select_country')"
            :options="countries"
            option-value="id"
            option-label="name"
            emit-value
            map-options
            @input="counrty_changed"
            v-model="selectedCountry"
            :rules="$helper.rules.select"
        />
    </div>
    <div class="input_div">
         <q-select
            :label="$t('select_region')"
            :options="regions"
            option-value="id"
            option-label="name"
            emit-value
            map-options
            @input="region_changed"
            v-model="selectedRegion"
            :rules="$helper.rules.select"
        />
    </div>

    <div class="input_div">
         <q-select
            :label="$t('select_district')"
            :options="districts"
            option-value="id"
            option-label="name"
            emit-value
            map-options
            v-model="patient.district"
            :rules="$helper.rules.select"
        />
    </div>

    <div class="input_div">
        <q-input
            clearable
            v-model="patient.address"
            :rules="rules.address"
            :label="$t('address_line')"
        />
    </div>

    <div class="input_div">
        <q-input
            clearable
            v-model="patient.fromdate"
            :label="$t('date_of_app')"
            type='date'
        />
    </div>

    <div class="input_div">
         <q-select
            :label="$t('select_occupation')"
            :options="occupations"
            option-value="id"
            option-label="title"
            emit-value
            map-options
            v-model="patient.occupation"
            :rules="$helper.rules.select"
        />
    </div>
    <div class="input_div">
        <q-input
            clearable
            v-model="patient.number"
            :label="$t('patient_number')"
            type='number'
            :rules="$helper.rules.number" 
        />
    </div>
  </div>
</q-form>
</template>

<script>
export default {
    props: ['patient'],
    data: function(){
        return {
            rules: {
                name : [
                    value => !!value || this.$t('required'),
                    value => (value && value.length >= 3) || this.$t('min_3_characters'),
                    value => /^[\w'][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*,.(){}|~<>;:[\]]{2,}$/.test(value) || this.$t('must_be_characters'),
                ],
                address: [
                    value => !!value || this.$t('required'),
                    value => (value && value.length >= 3) || this.$t('min_3_characters'),
                ],
                    select: [
                    value => !!value || this.$t('required'),
                ]
            },
            countries: [],
            selectedCountry: null,
            regions: [],
            selectedRegion: null,
            districts: [],
            occupations: [],
        }
    },
    methods: {
        initialize(){
            // Check for edidting
            if (typeof this.patient.id == 'undefined'){
                // Read the countries
                this.$axios.get('/countries')
                .then((response) => {
                    this.countries = response.data
                    if (this.countries.length > 0){
                        this.selectedCountry = this.countries[0].id
                        this.counrty_changed()
                    }
                })
                
                this.$axios.get('/occupations')
                .then(response => {
                    this.occupations = response.data
                    if (this.occupations.length > 0){
                        this.patient.occupation = this.occupations[0].id
                    }
                })
            }
            else{
                // to do when working editing
            }
        },
        counrty_changed(){
            this.$axios.get('/regions_by_country/' + this.selectedCountry)
            .then((response) => {
                this.regions = response.data
                if (this.regions.length > 0){
                    this.selectedRegion = this.regions[0].id
                    this.region_changed()
                }
            })
        },
        region_changed(){
            this.$axios.get('/districts_by_region/' + this.selectedRegion)
            .then((response) => {
                this.districts = response.data
                if (this.districts.length > 0){
                    this.patient.district = this.districts[0].id
                }
            })
        },
        hasError(){
            return this.$refs['form'].validate()
        }
    },
    beforeMount: function(){
        this.initialize()
    }
}
</script>

<style lang="scss" scoped>
    div.input_div{
        margin-left: 5px; margin-right: 5px; width: 200px
    }
</style>>