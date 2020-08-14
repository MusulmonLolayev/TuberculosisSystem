<template>
  <div>
    <v-row>
      <v-col 
      cols="10" 
      md="2" 
      v-for="(item, index) in labels"
      :key="index" >
        <v-text-field
        :label="item" 
        v-model="bloodanalysis[item]" 
        type="number" 
        :rules="[() => required(item)]"
        required
        min="0"
        :ref="item"
        dense
        validate-on-blur
        />
      </v-col>
      
      <v-col cols="10" md="2">
        <v-checkbox v-model="bloodanalysis.status" label="Status" />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field
          label="Date"
          v-model="bloodanalysis.date"
          type='date'
        />
      </v-col>
    </v-row>
    <div v-show="isError">
      <span class="red--text">Logical errors: {{logicalErrors.length}}</span>
        <v-simple-table height="100" dense>
          <template v-slot:default>
            <tbody>
              <tr v-for="(item, index) in logicalErrors" :key="index">
                <td>{{item.error}}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
</template>

<script>
import Helper from "../commons/functions.js";

export default {
  name: "v-blood-analysis",
  props: ["bloodanalysis", "check_acceptability"],
  data: function(){
    return{
      /* 
      {
        pair1: 'pair1_name',
        pair1: 'pair2_name',
        error: "error_text"
      }
      */
      logicalErrors: [],
      labels: ['er', 'leyk', 'hb', 'color', 'pya', 'sya', 'eoz', 'lf', 'mon', 'coe', 'act', 'alt'],
      rules: {
        er: [() => {return this.required('er')}],
        leyk: [() => {return this.required('leyk')}],
        hb: [() => {return this.required('hb')}],
        color: [() => {return this.required('color')}],
        pya: [() => {return this.required('pya')}],
        sya: [() => {return this.required('sya')}],
        eoz: [() => {return this.required('eoz')}],
        lf: [() => {return this.required('lf')}],
        mon: [() => {return this.required('mon')}],
        coe: [() => {return this.required('coe')}],
        act: [() => {return this.required('act')}],
        alt: [() => {return this.required('alt')}],
      }
    }
  },
  computed: {
    isError: function(){
      return this.logicalErrors.length
    }
  },
  methods: {
    initialize() {
      if (typeof this.bloodanalysis.id == "undefined") {
        this.bloodanalysis.er = 0;
        this.bloodanalysis.leyk = 0;
        this.bloodanalysis.hb = 0;
        this.bloodanalysis.color = 0;
        this.bloodanalysis.pya = 0;
        this.bloodanalysis.sya = 0;
        this.bloodanalysis.eoz = 0;
        this.bloodanalysis.lf = 0;
        this.bloodanalysis.mon = 0;
        this.bloodanalysis.hb = 0;
        this.bloodanalysis.coe = 0;
        this.bloodanalysis.act = 0;
        this.bloodanalysis.alt = 0;
        this.bloodanalysis.date = Helper.GetCurrentDate();
      }
    },
    required(name){
      let value = this.bloodanalysis[name]
      if (!value)
        return 'Required.'
      if (typeof this.check_acceptability != "undefined"){
        let res = this.check_acceptability(name, this.bloodanalysis)
        if (typeof res == 'boolean')
          return res
        Object.keys(res).forEach(item => {
            let t = -1
            for (let i = 0; i < this.logicalErrors.length; i++){
              let e = this.logicalErrors[i]
              if (
                e['feature_name1'] == name && e['feature_name2'] == res[item]['feature_name2']
                ||
                e['feature_name2'] == name && e['feature_name1'] == res[item]['feature_name2']
                ){
                t = i
                break
              }
            }
            if (t > -1){
              this.logicalErrors[t].error = res[item].error
            }
            else{
              this.logicalErrors.push(res[item])
            }
        })
        return res.length + " logical errors."  
      }
      return true
    },
    hasError(){
      let error = false
      this.labels.forEach(item => {
        let res = this.required(item)
        if (typeof res == 'string'){
          error = true
          if (this.$refs[item].hasError)
            this.$refs[item].validate(true)
        }
      })
      return error
    },
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style lang="scss" scoped>
</style>>
