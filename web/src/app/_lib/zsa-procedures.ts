import { ReportCreatorStreamService } from '@/services/report-creator-stream.service'
import { ReportCreatorService } from '@/services/report-creator.service'
import { UploadReportService } from '@/services/upload-report.service'
import { HttpClient } from '@/shared/http-client'
import { createServerActionProcedure } from 'zsa'

export const baseProcedure = createServerActionProcedure().handler(async () => {
  const httpClient = new HttpClient()
  const uploadReportService = new UploadReportService(httpClient)
  const reportCreatorService = new ReportCreatorService(httpClient)
  const reportCreatorStreamService = new ReportCreatorStreamService(httpClient)

  return {
    reportCreatorService,
    reportCreatorStreamService,
    uploadReportService,
  }
})
