export function login(context, {access_token, refresh_token}) {
    context.commit('login_success', {
        access_token: access_token, 
        refresh_token: access_token
    })
}

export function refresh_token(context){
    console.log(this.state.refresh_token)
    this.$axios.post('/login/refresh', {
        refresh: this.state.refresh_token
    })
    .then((response) => {
        console.log(response.data)
    })
    .catch(() => {
        this.$router.push('/login')
    })
}