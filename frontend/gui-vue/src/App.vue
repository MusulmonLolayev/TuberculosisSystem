<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item link @click="gotocreate">
          <v-list-item-action>
            <v-icon>mdi-folder-plus</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>Create</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link @click="gotodata">
          <v-list-item-action>
            <v-icon>mdi-database</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>Data</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link @click="gotodatamining">
          <v-list-item-action>
            <v-icon>mdi-database-search</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>Data mining</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        
        <v-divider />

        <v-list-item link @click="gotolog">
          <v-list-item-action>
            <v-icon>mdi-login</v-icon>
          </v-list-item-action>

          <v-list-item-content>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


    <v-app-bar 
      dense
      app
      clipped-left
    >
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <router-link to="/" class="router-link">Home</router-link>
      <router-link to="/news" class="router-link">News</router-link>
      <router-link to="/about" class="router-link">About</router-link>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn
    }
  },
  data: () => ({
    drawer: null,
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
  }
};
</script>

<style scoped>
  .router-link{
    margin-right: 10px;
    margin-left: 10px;
  }
</style>