<template>
  <v-app>
    
    <v-app-bar 
      color="primary"
      dense
      Collapse-On-Scroll
      app
      >
      <div>
        <router-link to="/home">Home</router-link>
        <router-link to="/news">News</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/create">Create</router-link>
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
};
</script>
