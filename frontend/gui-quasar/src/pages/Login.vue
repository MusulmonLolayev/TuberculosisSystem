<template>
  <q-card class="row justify-center q-pa-md">
    <q-layout>
      <span v-show="IsError">
        {{$t('username_or_password_incorrect')}}
      </span>
      <q-input v-model="username" :label="$t('user_or_email')" style="margin:5px"/>
      <q-input v-model="password" :type="isPwd ? 'password' : 'text'" :label="$t('password')" style="margin:5px">
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>
      <q-btn flat class="full-width" style="margin:5px" @click="login()">
        {{$t('login')}}
      </q-btn>
    </q-layout>
  </q-card>
</template>

<script>

export default {
  data: function(){
    return {
      isPwd: true,
      username: '',
      password: '',
      IsError: false
    }
  },
  methods: {
    login(){
      this.IsError = false
      this.$axios.post('/login', 
      {
          username: this.username,
          password: this.password
      })
      .then((response) => {
        this.$store.dispatch('auth/login',{
              access_token: response.data.access, 
              refresh_token: response.data.refresh
        })
        this.$router.go(-1)
      })
      .catch((error) => {
          if (error.response.status === 401)
            this.IsError = true
      })
    }
  }
}
</script>

<style scoped>
.login {
  width: 300px;
  height: 180px;
  align-self: center;
}
</style>