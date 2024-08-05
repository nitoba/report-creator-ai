"use client"

import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import React, { useState } from "react"

export function ReactQueryProvider({ children }: React.PropsWithChildren) {
  const [client] = useState(new QueryClient())

  return <QueryClientProvider client={client}>{children}</QueryClientProvider>
}