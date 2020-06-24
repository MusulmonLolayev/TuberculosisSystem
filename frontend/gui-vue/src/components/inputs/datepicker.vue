<template>
  <v-menu
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="290px"
    >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
        v-model="date"
        label="label"
        v-bind="attrs"
        v-on="on" />
    </template>
    <v-date-picker v-model="date" @input="menu = false"></v-date-picker>
  </v-menu>
</template>


<script>
export default {
  name: 'DatePicker',
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
  }),
  props:['label']
}
</script>
