import { z } from 'zod'

export const uploadReportSchema = z.object({
  title: z.string().optional(),
  content: z.string().min(1),
})

export type UploadReportBody = z.infer<typeof uploadReportSchema>
