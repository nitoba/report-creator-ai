import { ClipboardMinus, Stars } from 'lucide-react'
import Link from 'next/link'
import { Sidebar } from '../_components/sidebar'
import { Header } from '../_components/header'
import { PropsWithChildren } from 'react'
import { ReactQueryProvider } from '../_providers/react-query'

export default function DashboardLayout({ children }: PropsWithChildren) {
  return (
    <div className="grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]">
      <div className="hidden border-r bg-muted/40 md:block">
        <div className="flex h-full max-h-screen flex-col gap-2">
          <div className="flex h-14 items-center border-b px-4 lg:h-[60px] lg:px-6 justify-between">
            <Link href="/" className="flex items-center gap-2 font-semibold">
              <ClipboardMinus className="h-6 w-6" />
              <span className="">Report Creator AI</span>
            </Link>
            <Stars className="h-6 w-6" />
          </div>
          <Sidebar />
        </div>
      </div>
      <div className="flex flex-col">
        <ReactQueryProvider>
          <Header />
          {children}
        </ReactQueryProvider>
      </div>
    </div>
  )
}
