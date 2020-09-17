<template>
<q-form ref="form">
  <div>
    <div class="row">
      <div class="col-5" 
      v-for="(item, index) in labels"
      :key="index" >
        <q-input
        :label="$t(item)" 
        v-model="bloodanalysis[item]" 
        type="number" 
        :rules="[() => required(item)]"
        :ref="item"
        />
      </div>
      
      <div class="col-5">
        <q-checkbox v-model="bloodanalysis.status" :label="$t('status')" />
      </div>
      <div class="col-5">
        <q-input
          :label="$t('date')"
          v-model="bloodanalysis.date"
          type='date'
        />
      </div>
    </div>
    <div v-show="isError">
      <span class="red--text">{{$t('_logical_errors')}}: {{logicalErrors.length}}</span>
        <q-markup-table height="100" dense>          
            <tbody>
              <tr v-for="(item, index) in logicalErrors" :key="index">
                <td>{{item.error}}</td>
              </tr>
            </tbody>
        </q-markup-table>
      </div>
    </div>
</q-form>
</template>

<script>
export default {
  name: "BloodAnalysis",
  props: ["bloodanalysis", "check_acceptability"],
  data: function(){
    return{
      logicalErrors: [],
      labels: ['er', 'leyk', 'hb', 'color', 'pya', 'sya', 'eoz', 'lf', 'mon', 'coe', 'act', 'alt'],
    }
  },
  computed: {
    isError: function(){
      return this.logicalErrors.length
    }
  },
  methods: {
    initialize() {
    },
    required(name){
      let value = this.bloodanalysis[name]
      if (!value)
        return this.$t('required')
      
      this.logicalErrors = this.logicalErrors.filter(item => item['feature_name1'] != name && item['feature_name2'] != name)

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
        return res.length + " " + this.$t('logical_errors') + "."  
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
    hasError(){
      return this.$refs['form'].validate()
    }
  },
  beforeMount() {
    this.initialize();
  },
};
</script>

<style lang="scss" scoped>
</style>>
