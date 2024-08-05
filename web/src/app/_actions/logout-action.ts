'use server'
import { redirect } from 'next/navigation'
import { authenticatedProcedure } from '../_lib/zsa-procedures'
import { deleteSession } from '../_lib/session'

export const logoutAction = authenticatedProcedure
  .createServerAction()
  .handler(async () => {
    deleteSession()
    redirect('/sign-in')
  })
