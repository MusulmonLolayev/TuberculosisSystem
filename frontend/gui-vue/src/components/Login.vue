<template>
  <v-form>
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
                :append-icon="show4 ? 'mdi-eye' : 'mdi-eye-off'"
                label="Error"
                hint="At least 8 characters"
                value="Pa"
                error
                @click:append="show4 = !show4"
                v-model="password"
            />
        </v-list-item-content>
        </v-list-item>
        <v-card-actions>
            <v-btn text @click='login'>Login</v-btn>
        </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
export default {
    name: 'login',
    data: function(){
        return{
            username: '',
            password: ''
        }
    },
    methods: {
        login: function() {
            let username = this.username
            let password = this.password
            this.$store.dispatch('login', {username, password})
            .then(() => this.$router.push('/'))
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>

</style>