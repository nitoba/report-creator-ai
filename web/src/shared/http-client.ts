import axios, { Axios } from 'axios'
import { env } from './env/server'

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
  }
}

export const api = axios.create({
  baseURL: env.NEXT_PUBLIC_API_BASE_URL,
})
