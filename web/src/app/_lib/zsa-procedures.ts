import { AuthenticateUserService } from '@/services/authenticate-user.service'
import { RegisterUserService } from '@/services/register-user.service'
import { ReportCreatorService } from '@/services/report-creator.service'
import { UploadReportService } from '@/services/upload-report.service'
import { HttpClient } from '@/shared/http-client'
import { createServerActionProcedure } from 'zsa'

const httpClient = new HttpClient()

export const baseProcedure = createServerActionProcedure().handler(async () => {
  const authenticateUserService = new AuthenticateUserService(httpClient)
  const registerUserService = new RegisterUserService(httpClient)

  return {
    httpClient,
    authenticateUserService,
    registerUserService,
  }
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
