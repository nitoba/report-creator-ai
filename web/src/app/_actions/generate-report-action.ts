'use server'

import { authenticatedProcedure } from '../_lib/zsa-procedures'

export const generateReportAction = authenticatedProcedure
  .createServerAction()
  .handler(async ({ ctx }) => {
    const reportCreated = await ctx.reportCreatorService.execute()

    return reportCreated.report
  })
