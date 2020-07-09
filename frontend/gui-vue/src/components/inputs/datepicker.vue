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
        v-model="date.value"
        :label="label"
        v-bind="attrs"
        v-on="on" 
        @input="datechange"
        />
    </template>
    <v-date-picker v-model="date.value"  @input="datechange"></v-date-picker>
  </v-menu>
</template>


<script>
export default {
  name: 'DatePicker',
  data: () => ({
    //date: (typeof this.current_value == 'undefined') ? new Date() : Date.parse(this.current_value),
    menu: false,
  }),
  props: ['label', 'date', 'change'],
  methods: {
      datechange(){
        this.menu = false
        if (this.change)
          this.change()
      }
  }
}
</script>
