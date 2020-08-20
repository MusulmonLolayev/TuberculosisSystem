<template>
  <div>
      <div>
        <v-btn text @click="btnMean" :disabled='!isEnableUpdatingRangeButton'>Mean</v-btn>
        <v-btn text @click="btnMedian" :disabled='!isEnableUpdatingRangeButton'>Median</v-btn>
    </div>
      <!--<h2 v-if="isLoading">Loading.....</h2>
      <v-row>
          <v-col v-for="(item, index) in data" v-bind:key="index" cols='15' md='3'>
              ({{combination[index][0]}}, {{combination[index][1]}})-[{{item[0]}}, {{item[1]}}]
          </v-col>
      </v-row> -->
  </div>
</template>

<script>

import {Api} from '@/api/Api'
import Helper from '../commons/functions'

export default {
    name: 'v-data-mining',
    data: function(){
        return {
            data: {
            },
            names: ['Возрост', 'эр', 'лейк', 'Hb', 'Цв.', 'Пок.', 'П/я', 'С/я', 'эоз', 'Лф', 'мон', 'СОЭ', 'ACT', 'ALT'],
            combination: [],
            isLoading: true,
            GLOBAL_UPDATINGS: {
                hasUpdating: true,
                IsUpdatedRanges: true,
            }
        }
    },
    methods: {
        UPDATE_BY_API(method){
            Api.get('/updateaccetableintervals/' + method)
            .then((response) => {
                this.$store.state.alert.showMessage('Updated successfully', 
          Helper.message_types.success)
                this.GLOBAL_UPDATINGS = response.data
            })
        },
        makeFeatures(){
            for (let i = 0; i < this.names.length; i++){
                for (let j = i + 1; j < this.names.length; j++){
                    this.combination.push([this.names[i], this.names[j]])
                }
            }
        },
        btnMean(){
            this.UPDATE_BY_API('mean')    
        },
        btnMedian(){
            this.UPDATE_BY_API('median')    
        },
        initialize(){
            Api.get('/GetRangesUpdatingStatus').then((response) => {
                this.GLOBAL_UPDATINGS = response.data
            })
        }
    },
    mounted: function(){
        this.initialize()
    },
    computed: {
        isEnableUpdatingRangeButton(){
            return this.GLOBAL_UPDATINGS.hasUpdating && !this.GLOBAL_UPDATINGS.IsUpdatedRanges
        }
    }
}
</script>

<style>

</style>