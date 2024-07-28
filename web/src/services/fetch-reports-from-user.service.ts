import { HttpClient } from '@/shared/http-client'

type FetchReportsFromUserResponse = {
  id: string
  title: string
  file_id: string
  storage_url: string
  word_count: number
  created_at: string
  updated_at: string
}

export class FetchReportsFromUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute() {
    try {
      const response =
        await this.httpClient.get<FetchReportsFromUserResponse[]>('/reports')

      return response.data
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log('ERROR NO SERVICE', error.response?.data)
      throw new Error(error.response?.data)
    }
  }
}
