import {Api} from '@/api/Api.js'
export default {

    message_types: {
        success: 'success',
        error: 'error'
    },

    ToYesNO(value) {
        return value == true ? "Yes" : "No";
    },
    ToBoolFromYesNo(value) {
        return value == "Yes";
    },
    ToPlusMinus(value) {
        return value == true ? "+" : "-";
    },
    ToBoolFromPlusMinus(value) {
        return value == "+";
    },
    GetCurrentDate() {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        
        today = yyyy + '-' + mm + '-' + dd;
        return today
    },
    check_acceptability: function(name, instance, ranges){
        let res = [
  
        ]
        let names = Object.keys(instance)
        for (let i = 0; i < names.length; i++){
          
          let val1 = instance[name]
          let val2 = instance[names[i]]
          if (val2 && names[i] != name && !isNaN(val2)){
            ranges.forEach(item => {
              
              let f1 = item['feature_name1']
              let f2 = item['feature_name2'] 
              
              if (name == f1 && names[i] == f2 || name == f2 && names[i] == f1){
                
                let sub_val1 = item['sub_value1']
                let sub_val2 = item['sub_value2']
  
                let r_val = 0
  
                if (name == f1 && names[i] == f2){
                  //console.log(1)
                  r_val = val1 / sub_val1 - val2 / sub_val2
                }
                else{
                  //console.log(2)
                  r_val = val2 / sub_val1 - val1 / sub_val2
                }
  
                //r_val = val1 / sub_val1 - val2 / sub_val2
  
                let l_R = item['l_R']
                let r_R = item['r_R']
  
                if (r_val < l_R || r_R < r_val){
                  res.push({
                    feature_name1: name,
                    feature_name2: names[i],
                    error: `It can not be logically possible when ${name} has ${val1} and ${names[i]} has ${val2}`
                  })
                }
              }            
            });
          }
        }
        if (res.length > 0)
          return res
        return true
    },

    async saveInstance(instance, url){  
      try{
        if (typeof instance.id == "undefined") {
          let response = await Api
            .post(url, {
              instance
            })
          instance.id = response.data
          return true
        } else {
          await Api
            .put(url, {
              instance
            })
          return true
        }
      }
      catch (e){
        return e
      }
    },
}