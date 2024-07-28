import { ReportCreatorService } from '@/services/report-creator.service'
import { UploadReportService } from '@/services/upload-report.service'
import { HttpClient } from '@/shared/http-client'
import { createServerActionProcedure } from 'zsa'

const httpClient = new HttpClient()

export const baseProcedure = createServerActionProcedure().handler(async () => {
  return null
})

export const authenticatedProcedure = createServerActionProcedure().handler(
  async () => {
    const uploadReportService = new UploadReportService(httpClient)
    const reportCreatorService = new ReportCreatorService(httpClient)

    return {
      reportCreatorService,
      uploadReportService,
    }
  },
)
