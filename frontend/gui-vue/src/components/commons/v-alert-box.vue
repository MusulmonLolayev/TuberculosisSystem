<template>
  <v-snackbar :timeout="timeout" :value="show" :color='type' top right>
    <template v-slot:action="{ attrs }">
      <v-btn color="blue" text v-bind="attrs" @click="close">Close</v-btn>
    </template>
    {{message}}
  </v-snackbar>
</template>

<script>
export default {
  name: "v-alert-box",
  data: function(){
    return {
      timeout: 4000,
      show: false,
      type: '',
      message: '',
    }
  },
  methods: {
    showMessage(message='', type='success', timeout=2000){
      this.show = true
      this.message = message
      this.type = type
      this.timeout = timeout

      setTimeout(this.close, timeout)
    },
    close(){
      this.show = false
    }
  }
};
</script>

<style>
</style>