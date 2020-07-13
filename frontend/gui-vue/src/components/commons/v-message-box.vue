<template>
  <v-dialog
      v-model="data.dialog"
      max-width="300"
      :persistent='data.persistent'
    >
      <v-card>
        <v-card-title class="headline">
            {{data.title}}
        </v-card-title>
        <v-divider />
        <v-card-text>
          <v-alert
            :type='data.alert_type'
          >
            {{data.message}}
          </v-alert>
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="btnDisagree"
            :disabled='this.data.btnDisAgree == null'
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="btnAgree"
            :disabled='this.data.btnAgree == null'
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>

export default {
    name: 'v-message-box',
    props: ['data'],
    methods: {
        btnAgree: function() {
            this.data.dialog = false
            if (this.data.btnAgree != null){
              this.data.btnAgree()
            }
        },
        btnDisagree: function() {
            this.data.dialog = false
            if (this.data.btnDisAgree != null){
              this.data.btnDisAgree()
            }
        }
    },
}
</script>

<style>

</style>