export default function () {
  return {
    IsLoggined: false,
    access_token: localStorage.getItem('access_token'),
    refresh_token: localStorage.getItem('refresh_token'),    
  }
}
