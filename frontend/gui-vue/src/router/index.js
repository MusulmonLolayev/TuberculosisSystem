import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import About from '../components/About'
import Contact from '../components/Contact'
import News from '../components/News'
import Create from '../components/create/Create'

Vue.use(Router)

export default new Router({
    mode: 'history',
    hash: false,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/home',
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
            component: Create
        }
    ]
})