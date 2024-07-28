'use server'

import { ZSAError } from 'zsa'
import { baseProcedure } from '../_lib/zsa-procedures'
import { registerUserSchema } from '@/shared/dtos/register-user-schema'

export const registerUserAction = baseProcedure
  .createServerAction()
  .input(registerUserSchema)
  .handler(async ({ ctx, input }) => {
    try {
      await ctx.registerUserService.execute(input)
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log(error.message)
      throw new ZSAError('ERROR', error.message)
    }
  })
