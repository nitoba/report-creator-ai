'use server'

import { ZSAError } from 'zsa'
import { baseProcedure } from '../_lib/zsa-procedures'
import { authenticateUserSchema } from '@/shared/dtos/authenticate-user-schema'
import { createSession } from '../_lib/session'

export const authenticateUserAction = baseProcedure
  .createServerAction()
  .input(authenticateUserSchema)
  .handler(async ({ ctx: { authenticateUserService }, input }) => {
    try {
      const result = await authenticateUserService.execute(input)
      await createSession(result.access_token)

      return result
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log(error.message)
      throw new ZSAError('ERROR', error.message)
    }
  })
