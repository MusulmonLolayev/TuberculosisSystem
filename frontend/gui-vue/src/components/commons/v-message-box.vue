<template>
  <v-dialog
    v-model="dialog"
    max-width="350"
    :persistent='persistent'
     style="background-color:white"
  >
    <div style="width:350px">
      <v-alert :type='alert_type' max-width="350" margin="0px">
        {{message}}
      </v-alert>
      <div style="background-color:white" margin="0px">
        <v-btn
          color="green darken-1"
          text
          @click="dialog = false"
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
      </div>
    </div>
  </v-dialog>
</template>

<script>
import Helper from './functions'

export default {
    name: 'v-message-box',
    data: function(){
      return {
        dialog: false,
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
        showMessage(message, alert_type='success', persistent=false, btnAgree = null, btnDisAgree = null){
          this.dialog = true
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