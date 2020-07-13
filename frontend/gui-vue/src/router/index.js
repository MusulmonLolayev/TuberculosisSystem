import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import About from '../components/About'
import Contact from '../components/Contact'
import News from '../components/News'
import vCreate from '../components/create/v-create'
import Login from '../components/Login'
import store from '../vuex/store'
import Data from '../components/workplace/data'
import Detials from '../components/workplace/detials'
import DataMining from '../components/workplace/datamining'

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
            component: Data
        },
        {
            path: '/detials/:patient',
            name: 'detials',
            component: Detials
        },
        {
            path: '/datamining',
            name: 'datamining',
            component: DataMining
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