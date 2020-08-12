import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import About from '../components/About'
import Contact from '../components/Contact'
import News from '../components/News'
import vCreate from '../components/create/v-create'
import Login from '../components/Login'
import store from '../vuex/store'
import vData from '../components/workplace/v-data'
import vDetials from '../components/workplace/v-detials'
import vDataMining from '../components/workplace/v-data-mining'

Vue.use(Router)

var router = new Router({
    mode: 'history',
    hash: false,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/contact',
            name: 'contact',
            component: Contact
        },
        {
            path: '/news',
            name: 'news',
            component: News
        },
        {
            path: '/create',
            name: 'create',
            component: vCreate
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/data',
            name: 'data',
            component: vData
        },
        {
            path: '/detials/:patient',
            name: 'detials',
            component: vDetials
        },
        {
            path: '/datamining',
            name: 'datamining',
            component: vDataMining
        },
    ]
})

router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiresAuth)) {
      if (store.getters.isLoggedIn) {
        next()
        return
      }
      next('/login') 
    } else {
      next() 
    }
  })

export default router