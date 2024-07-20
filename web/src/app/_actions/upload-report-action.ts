'use server'

import { ZSAError } from 'zsa'
import { baseProcedure } from '../_lib/zsa-procedures'
import { uploadReportSchema } from '@/shared/dtos/upload-report-schema'

export const uploadReportAction = baseProcedure
  .createServerAction()
  .input(uploadReportSchema)
  .handler(async ({ ctx, input }) => {
    try {
      const reportCreated = await ctx.uploadReportService.execute(input)
      return {
        message: reportCreated.message,
      }
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log(error)
      throw new ZSAError('ERROR', error.message)
    }
  })
