'use server'

import { authenticatedProcedure } from '../_lib/zsa-procedures'
import { paginationInputSchema } from '@/shared/dtos/paginated-schema'

export const fetchReportsFromUserAction = authenticatedProcedure
  .createServerAction()
  .input(paginationInputSchema)
  .handler(async ({ ctx, input }) => {
    const reports = await ctx.fetchReportsFromUserService.execute(input)

    return reports
  })
