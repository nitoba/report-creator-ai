import { ReportCreatorStreamService } from '@/services/report-creator-stream.service'
import { useCallback, useRef, useState } from 'react'

const reportCreatorStreamService = new ReportCreatorStreamService()

export function useReportStreaming() {
  const [isGeneratingReport, setIsGeneratingReport] = useState(false)
  const [streamedContent, setStreamedContent] = useState('')
  const [finishedStreaming, setFinishedStreaming] = useState(false)
  const abortReportCreation = useRef<() => void>()
  const titleInputRef = useRef<HTMLInputElement>(null)

  function handleReset() {
    setIsGeneratingReport(false)
    setStreamedContent('')
    setFinishedStreaming(false)
    abortReportCreation.current = undefined
  }

  const handleGenerateReport = useCallback(async () => {
    handleReset()
    setIsGeneratingReport(true)
    const result = await reportCreatorStreamService.execute()

    if (!result) {
      setIsGeneratingReport(false)
      return
    }

    abortReportCreation.current = result.abort

    for await (const data of result.stream) {
      if (data.isDone) {
        setFinishedStreaming(true)
        break
      }
      setStreamedContent((prev) => prev + data.data)
      setIsGeneratingReport(false)
    }
  }, [])

  const handleAbortReportCreation = useCallback(() => {
    titleInputRef.current!.value = ''

    if (abortReportCreation.current) {
      abortReportCreation.current()
      setFinishedStreaming(true)
    }
  }, [])

  return {
    isGeneratingReport,
    streamedContent,
    finishedStreaming,
    titleInputRef,
    handleGenerateReport,
    handleAbortReportCreation,
    handleReset,
  }
}
