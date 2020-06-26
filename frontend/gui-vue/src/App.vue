<template>
  <v-app>
    
    <v-app-bar 
      color="primary"
      dense
      Collapse-On-Scroll
      app
      >
      <div>
        <router-link to="/">Home</router-link>
        <router-link to="/news">News</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/create">Create</router-link>
        <router-link to="/login">Login</router-link>
        <span v-if='isLoggedIn'>| <a @click="logout">Logout</a></span>
      </div>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
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
  methods: {
    logout: function(){
      this.$store.dispatch('logout')
      .then(() =>{
        this.$router.push('/login')
      })
    }
  }
};
</script>
