import axios from 'axios'

/*export const api = axios.create({
        baseURL: `http://127.0.0.1:8000/api`,
        withCredentials: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'common': '',
            //'token': ''
        }
    })*/

export default() => {
    return axios.create({
        baseURL: 'http://127.0.0.1:8000/api',
        //baseURL: 'http://192.168.137.1:8000/api',
        withCredentials: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'common': '',
            //'token': ''
        }
    })
}