import axios, { Axios } from 'axios'
import { env } from './env/server'
import { getRawSession } from '@/app/_lib/session'

export class HttpClient extends Axios {
  constructor() {
    super({
      transformResponse: (data) => {
        return JSON.parse(data)
      },
      transformRequest: (data) => {
        return JSON.stringify(data)
      },
      responseType: 'json',
      headers: {
        'Content-Type': 'application/json',
      },
      baseURL:
        typeof window === 'undefined'
          ? env.API_BASE_URL
          : env.NEXT_PUBLIC_API_BASE_URL,
      timeout: 1000 * 60 * 2, // 2 minutes
    })

    this.interceptors.request.use(async (config) => {
      if (typeof window !== 'undefined') {
        const token = localStorage.getItem('access_token')
        if (token) {
          config.headers.Authorization = `Bearer ${token}`
        }
      } else {
        const session = await getRawSession()

        if (session) {
          config.headers.Authorization = `Bearer ${session}`
        }
      }
      return config
    })
  }
}

export const api = axios.create({
  baseURL: env.NEXT_PUBLIC_API_BASE_URL,
})

api.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
  }
  return config
})
