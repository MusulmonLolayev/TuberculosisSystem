<template>
  <v-container>
      <v-row>
          <v-col cols='10' md='1'>
              <v-text-field label='CD3' v-model="immunogram.cd3" type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='CD4' v-model="immunogram.cd4"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='CD8' v-model="immunogram.cd8"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='CD20' v-model="immunogram.cd20"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='IgM' v-model="immunogram.igm"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='IgG' v-model="immunogram.igg"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='IgA' v-model="immunogram.iga"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='TgE' v-model="immunogram.tge"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='ACT' v-model="immunogram.act"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='ALT' v-model="immunogram.alt"  type='number'/>
          </v-col>
          <v-col cols='10' md='1'>
              <v-text-field label='coe' v-model="immunogram.coe"  type='number'/>
          </v-col>
      </v-row>
  </v-container>
</template>

<script>
export default {
    name: 'Immunogram',
    props: ['immunogram'],
}
</script>

<style>

</style>