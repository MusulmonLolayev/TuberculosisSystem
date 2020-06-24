import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Router from 'vue-router'
import Vuetify from 'vuetify/lib'
import vuetify from '@/plugins/vuetify' // path to vuetify export

Vue.use(Vuetify)
Vue.use(Router)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  template: '<App />',
  components: {App},
  vuetify
}).$mount('#app')
