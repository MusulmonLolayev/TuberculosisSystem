<template>
  <v-form style="margin-top: 20px">
    <v-card
    class="mx-auto"
    max-width="344"
    outlined
    right
    >
        <v-list-item three-line>
        <v-list-item-content>
            <div class="overline mb-4">Please fill the fields</div>
            <v-text-field
                label="User name"
                required
                v-model="username"/>
            <v-text-field
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                label="Password"
                hint="At least 8 characters"
                :type="show ? 'text' : 'password'"
                @click:append="show = !show"
                v-model="password"
            />
        </v-list-item-content>
        </v-list-item>
        <v-card-actions>
            <v-btn text @click='login()'>Login</v-btn>
        </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
export default {
    name: 'v-login',
    data: function(){
        return{
            username: '',
            password: '',
            show: false,
        }
    },
    methods: {
        async login() {
            let username = this.username
            let password = this.password
            //let response = await 
            this.$store.dispatch('login', {username, password})
            
            //response == true && this.$router.go(-1)
        }
    }
}
</script>

<style>

</style>