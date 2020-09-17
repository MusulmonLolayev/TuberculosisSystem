export function login(context, {access_token, refresh_token}) {
    context.commit('login_success', {
        access_token: access_token, 
        refresh_token: access_token
    })
}

export function refresh_token(context){
    delete this.$axios.defaults.headers.common["Authorization"]
    console.log(this.$axios.defaults.headers.common)
    this.$axios.post('/login/refresh', {
        refresh: this.state.auth.refresh_token
    })
    .then((response) => {
        console.log(response.data)
        this.$axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`
        context.commit('refresh_token', {refresh_token: response.data.access})
    })
    .catch(() => {
        this.$router.push('/login')
    })
}