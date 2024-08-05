import {
  PaginatedSchema,
  PaginationInput,
} from '@/shared/dtos/paginated-schema'
import { HttpClient } from '@/shared/http-client'

type FetchReportsFromUserResponse = {
  id: string
  title: string
  user_id: string
  file_id: string
  storage_url: string
  word_count: number
  created_at: string
}

export class FetchReportsFromUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute(request: PaginationInput) {
    try {
      await new Promise((resolve) => setTimeout(resolve, 1000))
      const response = await this.httpClient.get<
        PaginatedSchema<FetchReportsFromUserResponse>
      >('/reports', {
        params: request,
      })

      return response.data
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log('ERROR NO SERVICE', error.response?.data)
      throw new Error(error.response?.data)
    }
  }
}
