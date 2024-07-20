'use client'

import React from 'react'
import { Button } from './ui/button'
import { generateReportAction } from '../_actions/generate-report-action'
import { useServerAction } from 'zsa-react'
import { ContentMarkdown } from './markdown'
import { Loader2 } from 'lucide-react'
import { cn } from '../_lib/utils'
import { Input } from './ui/input'
import { Label } from './ui/label'
import { uploadReportAction } from '../_actions/upload-report-action'
import { toast } from 'sonner'

export function Main() {
  const titleInputRef = React.useRef<HTMLInputElement>(null)
  const {
    data: report,
    reset: resetReport,
    isPending: isGeneratingReport,
    execute: handleGenerateReport,
  } = useServerAction(generateReportAction)

  const { isPending: isUploadingReport, execute: handleUploadReport } =
    useServerAction(uploadReportAction, {
      onSuccess: (result) => {
        toast.success(result.data.message)
        resetReport()
        titleInputRef.current!.value = ''
      },

      onError: (error) => {
        toast.error(error.err.data)
        console.log(error.err)
      },
    })

  const isReportGenerated = !!report

  function handleAbortReportCreation() {
    resetReport()
    titleInputRef.current!.value = ''
  }

  return (
    <main className="flex flex-1 flex-col gap-4 p-4 lg:gap-6 lg:p-6">
      <div className="flex items-center">
        <h1 className="text-lg font-semibold md:text-2xl">Reports</h1>
      </div>
      <div
        className="flex flex-1 items-center justify-center rounded-lg border border-dashed shadow-sm"
        x-chunk="dashboard-02-chunk-1"
      >
        {!isReportGenerated && (
          <div
            className={cn('flex flex-col items-center gap-1 text-center', {
              'animate-pulse': isGeneratingReport,
            })}
          >
            <h3 className="text-2xl font-bold tracking-tight">
              You have no reports
            </h3>
            <p className="text-sm text-muted-foreground">
              You can start send your first report by clicking the button below.
            </p>
            <Button
              className="mt-4"
              onClick={() => handleGenerateReport()}
              disabled={isGeneratingReport}
            >
              Create Report
              {isGeneratingReport && (
                <Loader2 className="ml-2 h-4 w-4 animate-spin" />
              )}
            </Button>
          </div>
        )}

        {isReportGenerated && (
          <div className="px-4 max-w-4xl w-full flex flex-col gap-6 h-full justify-center items-center py-10 animate-in fade-in-0 duration-300">
            <Label className="w-full space-y-2">
              <span className="text-sm">Report Title</span>
              <Input
                placeholder="Type your report title (optional)"
                ref={titleInputRef}
                disabled={isUploadingReport}
              />
            </Label>
            <ContentMarkdown content={report} />
            <div className="space-y-4 mt-auto w-full">
              <div className="w-full gap-2 flex">
                <Button
                  variant="secondary"
                  className="w-full"
                  disabled={isUploadingReport}
                  onClick={() => {
                    resetReport()
                    titleInputRef.current!.value = ''
                    handleGenerateReport()
                  }}
                >
                  Generate again
                </Button>
                <Button
                  className="w-full"
                  disabled={isUploadingReport}
                  onClick={() => {
                    handleUploadReport({
                      content: report,
                      ...(titleInputRef.current?.value && {
                        title: titleInputRef.current.value.trim(),
                      }),
                    })
                  }}
                >
                  Upload Report
                  {isUploadingReport && (
                    <Loader2 className="ml-2 h-4 w-4 animate-spin" />
                  )}
                </Button>
              </div>
              <Button
                variant="destructive"
                className="w-full"
                disabled={isUploadingReport}
                onClick={handleAbortReportCreation}
              >
                Abort Report
              </Button>
            </div>
          </div>
        )}
      </div>
    </main>
  )
}
