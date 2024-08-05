'use client'

import { QueryClientProvider } from '@tanstack/react-query'
import React from 'react'
import { queryClient } from '../_lib/query-client'

export function ReactQueryProvider({ children }: React.PropsWithChildren) {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  )
}
