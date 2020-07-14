<template>
  <v-snackbar :timeout="alert.timeout" :value="alert.show" :color='alert.type' top right>
    <template v-slot:action="{ attrs }">
      <v-btn color="blue" text v-bind="attrs" @click="alert.show = false">Close</v-btn>
    </template>
    {{alert.message}}
  </v-snackbar>
</template>

<script>
export default {
  name: "v-alert-box",
  props: ["alert"],
};
</script>

<style>
</style>