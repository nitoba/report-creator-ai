import { z } from 'zod'

export const userSchema = z.object({
  id: z.string(),
  username: z.string(),
  email: z.string().email(),
  created_at: z.coerce.date(),
  updated_at: z.coerce.date(),
})
