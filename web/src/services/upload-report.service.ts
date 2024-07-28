import { UploadReportBody } from '@/shared/dtos/upload-report-schema'
import { HttpClient } from '@/shared/http-client'

type UploadReportResponse = {
  message: string
}

export class UploadReportService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute({ content, title }: UploadReportBody) {
    try {
      const response = await this.httpClient.post<UploadReportResponse>(
        '/reports/upload',
        {
          title,
          content,
        },
      )
      console.log(response.data)
      return response.data
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log('ERROR NO SERVICE', error.response?.data)
      throw new Error(error.response?.data)
    }
  }
}
