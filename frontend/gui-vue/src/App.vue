<template>
<div>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >

      <v-list>
        <v-list-item dense to = '/' link>
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>

          <v-list-item-title>Home</v-list-item-title>
        </v-list-item>

      <v-list-group
        prepend-icon="mdi-database"
        dense
      >
        <template v-slot:activator>
          <v-list-item-title>Data</v-list-item-title>
        </template>

        <v-list-item link dense to='/create' style='margin-left:20px'>
          <v-list-item-action>
            <v-icon>mdi-account-multiple-plus</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>New Patient</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link dense to='/data' style='margin-left:20px'>
          <v-list-item-action>
            <v-icon>mdi-account-multiple</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>My patients</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

      </v-list-group>

      <v-list-group
        prepend-icon="mdi-database"
        dense
      >
        <template v-slot:activator>
          <v-list-item-title>Intellectual analysis</v-list-item-title>
        </template>

        <v-list-item link dense to='/datamining' style='margin-left:20px'>
          <v-list-item-action>
            <v-icon>mdi-square-edit-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Data mining</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>

      <v-list-group
        prepend-icon="mdi-account"
        dense
      >
        <template v-slot:activator>
          <v-list-item-title>Account</v-list-item-title>
        </template>

        <v-list-item link dense to='/editaccount' style='margin-left:20px'>
          <v-list-item-action>
            <v-icon>mdi-square-edit-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-navigation-drawer>


    <v-app-bar 
      dense
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>{{$store.state.nav_title}}</v-toolbar-title>
      
      <v-spacer></v-spacer>


      <v-menu
        transition="slide-y-transition"
      >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-bind="attrs"
          v-on="on"
          text
        >
          {{langueges[selectedLanguage].title}}<v-icon right>mdi-menu-down</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, i) in langueges"
          :key="i"
          @click="ChangedLanguage(i)"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
      <!--<router-link to="/" class="router-link">Home</router-link>
      <router-link to="/news" class="router-link">News</router-link>
      <router-link to="/about" class="router-link">About</router-link>-->
    
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <v-container fluid>
        <!-- Loader -->
        <v-overlay :value="$store.state.loader" absolute light>
          <v-progress-circular size="64"></v-progress-circular>
        </v-overlay>
        <!-- Alert and message box -->
        <v-message-box ref="message"/>
        <v-alert-box ref="alert"/>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</div>
</template>

<script>
import {Api} from './api/Api'
import store from './vuex/store.js'
import vMessageBox from "./components/commons/v-message-box";
import vAlertBox from "./components/commons/v-alert-box.vue"


export default {
  name: 'App',
  data: () => ({
    drawer: null,
    langueges: [
      {title: "English", key: 'en'},
      {title: "Russian", key: 'ru'},
      {title: "Uzbek", key: 'uz'},
    ],
    selectedLanguage: 0,
    admins: [
        ['Management', 'people_outline'],
        ['Settings', 'settings'],
      ],
      cruds: [
        ['Create', 'add'],
        ['Read', 'insert_drive_file'],
        ['Update', 'update'],
        ['Delete', 'delete'],
      ],
    mnuCreate: false,
  }),
  methods: {
    logout: function(){
      this.$store.dispatch('logout')
      .then(() =>{
        this.$router.push('/logout')
      })
    },
    gotocreate: function(){      
        this.$router.push('/create')
    },
    gotolog: function(){      
        this.$router.push('/login')
    },
    gotodata: function(){
      this.$router.push('/data')
    },
    gotodatamining: function(){
      this.$router.push('/datamining')
    },
    ChangedLanguage(index){
      this.selectedLanguage = index
    }
  },
  created() {
    // Add a request interceptor
    Api.interceptors.request.use(function (config) {
        // Do something before request is sent
        store.commit('LOADER', true)
        return config;
    }, function (error) {
    // Do something with request error
      store.commit('LOADER', false)
      return Promise.reject(error);
    });

    // Add a response interceptor
    Api.interceptors.response.use(function (response) {
        // Any status code that lie within the range of 2xx cause this function to trigger
        // Do something with response data
        store.commit('LOADER', false)
        return response;
      }, function (error) {
        // Any status codes that falls outside the range of 2xx cause this function to trigger
        // Do something with response error
        store.commit('LOADER', false)
        return Promise.reject(error);
      });
  },
  mounted(){
    store.state.alert = this.$refs['alert']
    store.state.message = this.$refs['message']
  },
  components: {
    vMessageBox,
    vAlertBox,
  },

};
</script>

<style scoped>
  .router-link{
    margin-right: 10px;
    margin-left: 10px;
  }
  v-list-group.inner v-list-item {
    margin-left:30px;
  }
</style>