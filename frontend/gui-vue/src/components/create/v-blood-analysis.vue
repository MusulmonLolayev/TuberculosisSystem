<template>
  <div>
    <v-row>
      <v-col cols="10" md="2">
        <v-text-field 
        label="er" 
        v-model="bloodanalysis.er" 
        type="number" 
        :rules="rules.er"
        required
        min="0"
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="leyk" 
        v-model="bloodanalysis.leyk" 
        type="number" 
        :rules="rules.leyk"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="hb" 
        v-model="bloodanalysis.hb" 
        type="number" 
        :rules="rules.hb"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="color" 
        v-model="bloodanalysis.color" 
        type="number" 
        :rules="rules.color"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="pya" 
        v-model="bloodanalysis.pya" 
        type="number" 
        :rules="rules.pya"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="sya" 
        v-model="bloodanalysis.sya" 
        type="number" 
        :rules="rules.sya"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="eoz" 
        v-model="bloodanalysis.eoz" 
        type="number" 
        :rules="rules.eoz"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="lf" 
        v-model="bloodanalysis.lf" 
        type="number" 
        :rules="rules.lf"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="mon" 
        v-model="bloodanalysis.mon" 
        type="number" 
        :rules="rules.mon"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="coe" 
        v-model="bloodanalysis.coe" 
        type="number" 
        :rules="rules.coe"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="act" 
        v-model="bloodanalysis.act" 
        type="number" 
        :rules="rules.act"
        required
        />
      </v-col>
      <v-col cols="10" md="2">
        <v-text-field 
        label="alt" 
        v-model="bloodanalysis.alt" 
        type="number" 
        :rules="rules.alt"
        required
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
    <div>
      <h2>Logical errors:</h2>
      <div class="error-container">
        <p v-for="(item, index) in logicalErrors" :key='index'>
          {{item}}
        </p>
      </div>
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
      rules: {
        er: [(value) => {return this.required(value, 'er')}],
        leyk: [(value) => {return this.required(value, 'leyk')}],
        hb: [(value) => {return this.required(value, 'hb')}],
        color: [(value) => {return this.required(value, 'color')}],
        pya: [(value) => {return this.required(value, 'pya')}],
        sya: [(value) => {return this.required(value, 'sya')}],
        eoz: [(value) => {return this.required(value, 'eoz')}],
        lf: [(value) => {return this.required(value, 'lf')}],
        mon: [(value) => {return this.required(value, 'mon')}],
        coe: [(value) => {return this.required(value, 'coe')}],
        act: [(value) => {return this.required(value, 'act')}],
        alt: [(value) => {return this.required(value, 'alt')}],
      }
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
    required(value, name){
      if (!value)
        return 'Required.'
      if (typeof this.check_acceptability != "undefined"){
        let res = this.check_acceptability(name, this.bloodanalysis)
        if (typeof res == 'boolean')
          return res
        this.logicalErrors.concat(res)
        return res.length + " logical errors."  
      }
      return true
    }
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style lang="scss" scoped>
.error-container {
    height: 100px;
    overflow-y: scroll;
    overflow-x:hidden;
}
</style>>
