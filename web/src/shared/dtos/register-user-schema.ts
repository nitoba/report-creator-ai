import { z } from 'zod'

export const registerUserSchema = z.object({
  username: z.string(),
  email: z.string().email(),
  password: z.string().min(6),
})

export type RegisterUserBody = z.infer<typeof registerUserSchema>
