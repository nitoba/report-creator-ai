import { z } from 'zod'

export type PaginatedSchema<T> = {
  data: T[]
  total: number
  page: number
  size: number
}

export const paginatedSchema = <T>(schema: z.ZodType<T>) => {
  return z.object({
    data: z.array(schema),
    total: z.number(),
    page: z.number(),
    size: z.number(),
  })
}

export const paginationInputSchema = z.object({
  page_index: z.number().optional(),
  page_size: z.number().optional(),
})

export type PaginationInput = z.infer<typeof paginationInputSchema>
