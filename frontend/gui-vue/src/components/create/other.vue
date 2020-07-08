<template>
  <v-container>
      <v-row>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.tuberculosis_tolerance"
                label="Tuberculosis tolerance"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.related_disease"
                label="Related disease"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.nausea"
                label="Nausea"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.vomiting"
                label="Vomiting"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.headache"
                label="Headache"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.sweating"
                label="Sweating"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.weakness"
                label="Weakness"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.allergodermatosis"
                label="Allergodermatosis"
                />
          </v-col>
          <v-col cols='10' md='2'>
              <v-checkbox
                v-model="other.coproscopy"
                label="Coproscopy"
                />
          </v-col>
          <v-col cols='10' md='3'>
            Weight loss: 
            <v-text-field v-model="other.from_weight_loss" label='from' type='number'/>
            <v-text-field v-model="other.to_weight_loss" label='to' type='number'/>
           </v-col>
      </v-row>
  </v-container>
</template>

<script>
export default {
    name: 'Other',
    props: ['other'],
}
</script>

<style>

</style>