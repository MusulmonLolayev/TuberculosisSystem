<template>
  <v-app>
    
    <v-app-bar 
      dense
      Collapse-On-Scroll
      app
      >
        <router-link to="/" class="router-link">Home</router-link>
        <router-link to="/news" class="router-link">News</router-link>
        <router-link to="/about" class="router-link">About</router-link>
        <router-link to="/create" class="router-link">Create</router-link>
        <router-link to="/login" class="router-link">Login</router-link>
        <span v-if='isLoggedIn' class="router-link"><a @click="logout">Logout</a></span>
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
        this.$router.push('/logout')
      })
    }
  }
};
</script>

<style scoped>
  .router-link{
    margin-right: 10px;
    margin-left: 10px;
  }
</style>