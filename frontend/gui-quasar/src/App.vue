<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  data: function(){
    return {
      title: '',
    }
  },
  methods: {
    initialize(){
      this.title = this.$t('app_name')
    }
  },

  meta() {
    return {
      title: this.$t('app_name'),
    };
  },
  mounted: function(){
    this.initialize()
  }
}
</script>
