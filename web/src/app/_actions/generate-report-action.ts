'use server'

import { baseProcedure } from '../_lib/zsa-procedures'

export const generateReportAction = baseProcedure
  .createServerAction()
  .handler(async ({ ctx }) => {
    const reportCreated = await ctx.reportCreatorService.execute()

    return reportCreated.report
  })
