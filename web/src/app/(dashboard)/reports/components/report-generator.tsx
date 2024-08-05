'use client'

import React from 'react'
import { useServerAction } from 'zsa-react'
import { Loader2 } from 'lucide-react'

import { toast } from 'sonner'
import { useReportStreaming } from '@/app/_hooks/useReportStreaming'
import { uploadReportAction } from '@/app/_actions/upload-report-action'
import { cn } from '@/app/_lib/utils'
import { Button } from '@/app/_components/ui/button'
import { Label } from '@/app/_components/ui/label'
import { Input } from '@/app/_components/ui/input'
import { ContentMarkdown } from '@/app/_components/markdown'
import { AlertDialogCancel } from '@/app/_components/ui/alert-dialog'

type ReportGeneratorProps = {
  onUploadedReport: () => void
}

export function ReportGenerator({ onUploadedReport }: ReportGeneratorProps) {
  const {
    finishedStreaming,
    handleAbortReportCreation,
    handleGenerateReport,
    handleReset,
    isGeneratingReport,
    streamedContent,
    titleInputRef,
  } = useReportStreaming()

  const { isPending: isUploadingReport, execute: handleUploadReport } =
    useServerAction(uploadReportAction, {
      onSuccess: (result) => {
        toast.success(result.data.message)
        titleInputRef.current!.value = ''
        onUploadedReport()
      },

      onError: (error) => {
        toast.error(error.err.data)
        console.log(error.err)
      },
    })

  const isStreamingData = streamedContent !== ''

  return (
    <div
      className="p-6 flex flex-1 items-center justify-center rounded-lg border border-dashed shadow-sm"
      x-chunk="dashboard-02-chunk-1"
    >
      {!isStreamingData && (
        <div
          className={cn('flex flex-col items-center gap-1 text-center w-full', {
            'animate-pulse': isGeneratingReport,
          })}
        >
          <h3 className="text-4xl font-bold tracking-tight">Generate Report</h3>
          <p className="text-muted-foreground">
            To start clicking the button below.
          </p>
          <div className="flex flex-col gap-4 mt-4 w-1/2">
            <Button
              className="w-full"
              onClick={() => handleGenerateReport()}
              disabled={isGeneratingReport}
            >
              Create Report
              {isGeneratingReport && (
                <Loader2 className="ml-2 h-4 w-4 animate-spin" />
              )}
            </Button>
            <AlertDialogCancel asChild disabled={isGeneratingReport}>
              <Button className="w-full" variant="outline">
                Cancel
              </Button>
            </AlertDialogCancel>
          </div>
        </div>
      )}

      {isStreamingData && (
        <div className="px-4 max-w-4xl w-full flex flex-col gap-6 h-full justify-center items-center py-10 animate-in fade-in-0 duration-300">
          <Label className="w-full space-y-2">
            <span className="text-sm">Report Title</span>
            <Input
              placeholder="Type your report title (optional)"
              ref={titleInputRef}
              disabled={isUploadingReport}
            />
          </Label>
          <ContentMarkdown content={streamedContent} />
          <div className="space-y-4 mt-auto w-full">
            <div className="w-full gap-2 flex">
              {finishedStreaming && (
                <>
                  <Button
                    variant="secondary"
                    className="w-full"
                    disabled={isUploadingReport || !finishedStreaming}
                    onClick={() => {
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
                        title: titleInputRef.current!.value,
                        content: streamedContent,
                      })
                    }}
                  >
                    Upload Report
                    {isUploadingReport && (
                      <Loader2 className="ml-2 h-4 w-4 animate-spin" />
                    )}
                  </Button>
                </>
              )}
            </div>

            {!finishedStreaming ? (
              <Button
                variant="destructive"
                className="w-full"
                disabled={isUploadingReport}
                onClick={handleAbortReportCreation}
              >
                Abort Report Generation
              </Button>
            ) : (
              <Button
                variant="destructive"
                className="w-full"
                disabled={isUploadingReport || !finishedStreaming}
                onClick={handleReset}
              >
                Cancel
              </Button>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
