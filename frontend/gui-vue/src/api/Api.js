import axios from 'axios'

export const Api = axios.create({
        baseURL: `http://127.0.0.1:8000/api`,
        withCredentials: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'common': '',
            //'token': ''
        }
})