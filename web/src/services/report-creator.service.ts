import { HttpClient } from '@/shared/http-client'

type ReportCreatorResponse = {
  report: string
}

export class ReportCreatorService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute(): Promise<ReportCreatorResponse> {
    const response = await this.httpClient.post('/generate-report')

    return {
      report: response.data.report,
    }
  }
}
