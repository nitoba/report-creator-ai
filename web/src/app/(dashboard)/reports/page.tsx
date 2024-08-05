'use client'

import { Button } from '@/app/_components/ui/button'
import { ReportsList } from './components/reports-list'
import { PlusCircle } from 'lucide-react'
import {
  AlertDialog,
  AlertDialogContent,
  AlertDialogTrigger,
} from '@/app/_components/ui/alert-dialog'
import { ReportGenerator } from './components/report-generator'
import { useState } from 'react'
import { useQueryClient } from '@tanstack/react-query'
import { queryClient } from '@/app/_lib/query-client'

export default function ReportsPage() {
  const qClient = useQueryClient(queryClient)
  const [reportGeneratorIsOpen, setReportGeneratorIsOpen] = useState(false)
  function onUploadedReport() {
    setReportGeneratorIsOpen(false)
    qClient.invalidateQueries({ queryKey: ['reports'] })
  }
  return (
    <main className="p-4 lg:gap-6 lg:p-6 flex flex-col gap-4">
      <AlertDialog
        open={reportGeneratorIsOpen}
        onOpenChange={setReportGeneratorIsOpen}
      >
        <header className="flex items-center justify-between">
          <div className="flex flex-col gap-1">
            <h1 className="text-lg font-semibold md:text-2xl">Reports</h1>
            <p className="text-sm text-muted-foreground">
              Manage your reports and view their work performance.
            </p>
          </div>
          <AlertDialogTrigger asChild>
            <Button size="sm">
              <PlusCircle className="size-4 mr-1" /> Add Report
            </Button>
          </AlertDialogTrigger>
        </header>

        <ReportsList />

        <AlertDialogContent className="max-w-7xl">
          <ReportGenerator onUploadedReport={onUploadedReport} />
        </AlertDialogContent>
      </AlertDialog>
    </main>
  )
}
