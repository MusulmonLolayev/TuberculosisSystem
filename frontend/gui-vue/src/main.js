import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Router from 'vue-router'
import Vuetify from 'vuetify/lib'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import store from './vuex/store'
import Axios from 'axios'

Vue.use(Vuetify)
Vue.use(Router)

Vue.config.productionTip = false

Vue.prototype.$http = Axios
const token = localStorage.getItem('token')

if (token){
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  template: '<App />',
  components: {App},
  vuetify,
  store
}).$mount('#app')
