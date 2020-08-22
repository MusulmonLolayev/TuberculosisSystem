import axios from 'axios'

export const Api = axios.create({
        baseURL: 'http://localhost:8000/api',
        headers: { contentType: 'application/json' }
})