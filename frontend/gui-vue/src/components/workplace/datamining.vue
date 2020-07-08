<template>
  <div>
    <div>
        <v-btn text @click="btnMean">Mean</v-btn>
        <v-btn text @click="btnMedian">Median</v-btn>
    </div>
      <h2 v-if="isLoading">Loading.....</h2>
      <v-row>
          <v-col v-for="(item, index) in data" v-bind:key="index" cols='15' md='3'>
              ({{combination[index][0]}}, {{combination[index][1]}})-[{{item[0]}}, {{item[1]}}]
          </v-col>
      </v-row>
  </div>
</template>

<script>

import Api from '@/api/Api'

export default {
    name: 'DataMining',
    data: function(){
        return {
            data: {
            },
            names: ['Возрост', 'эр', 'лейк', 'Hb', 'Цв.', 'Пок.', 'П/я', 'С/я', 'эоз', 'Лф', 'мон', 'СОЭ', 'ACT', 'ALT'],
            combination: [],
            isLoading: true
        }
    },
    methods: {
        GER_DATA_FROM_API(method){
            let self = this

            Api().get('/getaccetableintervals/' + method)
            .then((response) => {
                self.data = response.data
            })
            .catch((error) => {
                console.error(error)
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
            this.GER_DATA_FROM_API('mean')    
        },
        btnMedian(){
            this.GER_DATA_FROM_API('median')    
        },
    },
    mounted: function(){
        this.GER_DATA_FROM_API('mean')
        this.makeFeatures()
        this.isLoading = false
    }
}
</script>

<style>

</style>