export function login_success(state, {access_token, refresh_token}){
    state.IsLoggined = true
    localStorage.setItem('access_token', access_token)
    localStorage.setItem('refresh_token', refresh_token)
}
