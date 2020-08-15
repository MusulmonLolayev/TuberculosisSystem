<template>
  <v-dialog
      v-model="dialog"
      max-width="300"
      :persistent='persistent'
    >
      <v-card>
        <v-card-title class="headline">
            {{title}}
        </v-card-title>
        <v-divider />
        <v-spacer></v-spacer>
        <v-card-text>
          <v-alert
            :type='alert_type'
          >
            {{message}}
          </v-alert>
        </v-card-text>
        <v-divider />
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
            v-if='persistent'
          >
            Close
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="self_btnDisAgree"
            v-if='showDisAgree'
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="self_btnAgree"
            v-if='showAgree'
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import Helper from './functions'

export default {
    name: 'v-message-box',
    data: function(){
      return {
        dialog: false,
        title: '',
        message: '',
        alert_type: Helper.message_types.success,
        persistent: '',
        btnAgree: null,
        btnDisAgree: null,
      }
    },
    computed: {
      showAgree: function(){
        return this.btnAgree
      },
      showDisAgree: function(){
        return this.btnDisAgree
      },
    },
    methods: {
        self_btnAgree: function() {
            this.dialog = false
            this.btnAgree()
        },
        self_btnDisAgree: function() {
            this.dialog = false
            this.btnDisAgree()
        },
        showMessage(title, message, alert_type='success', persistent=false, btnAgree = null, btnDisAgree = null){
          this.dialog = true
          this.title = title
          this.message = message
          this.alert_type = alert_type
          this.persistent = persistent
          
          this.btnAgree = btnAgree
          this.btnDisAgree = btnDisAgree
        },

        closeMessage(){
          this.dialog = false
        }
    },
}
</script>

<style>

</style>