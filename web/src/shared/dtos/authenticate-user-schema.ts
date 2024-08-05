import { z } from 'zod'
import { userSchema } from './user-schema'

export const authenticateUserSchema = z.object({
  email: z.string().email(),
  password: z.string().min(6),
})

export const authenticatedUserResponse = z.object({
  access_token: z.string(),
  user: userSchema,
})

export type AuthenticatedUserResponse = z.infer<
  typeof authenticatedUserResponse
>

export type AuthenticateUserBody = z.infer<typeof authenticateUserSchema>
