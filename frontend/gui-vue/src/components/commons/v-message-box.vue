<template>
  <v-dialog
      v-model="message.dialog"
      max-width="300"
      :persistent='message.persistent'
    >
      <v-card>
        <v-card-title class="headline">
            {{message.title}}
        </v-card-title>
        <v-divider />
        <v-spacer></v-spacer>
        <v-card-text>
          <v-alert
            :type='message.alert_type'
          >
            {{message.message}}
          </v-alert>
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="btnDisagree"
            v-if='this.message.btnDisAgree != null'
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="btnAgree"
            v-if='this.message.btnAgree != null'
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
    props: ['message'],
    methods: {
        btnAgree: function() {
            this.message.dialog = false
            if (this.message.btnAgree != null){
              this.message.btnAgree()
            }
        },
        btnDisagree: function() {
            this.message.dialog = false
            if (this.message.btnDisAgree != null){
              this.message.btnDisAgree()
            }
        }
    },
}
</script>

<style>

</style>