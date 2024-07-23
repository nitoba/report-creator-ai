import {
  getIterableStream,
  IterableStreamResponse,
} from '@/app/_lib/stream-response'
import { env } from '@/shared/env/server'

let controller = new AbortController()
let signal = controller.signal

type ReportCreatorResponse = {
  stream: AsyncIterable<IterableStreamResponse>
  abort: () => void
} | null

function abortReportCreation() {
  try {
    controller.abort()
  } catch (error) {
    console.log(error)
  }
}

export class ReportCreatorStreamService {
  async execute(): Promise<ReportCreatorResponse> {
    try {
      if (signal.aborted) {
        controller = new AbortController()
        signal = controller.signal
      }
      const streamResponse = await fetch(
        `${env.NEXT_PUBLIC_API_BASE_URL}/generate-report-stream`,
        { signal },
      )

      if (streamResponse.status !== 200)
        throw new Error(streamResponse.status.toString())

      return {
        stream: getIterableStream(streamResponse.body!),
        abort: abortReportCreation,
      }
    } catch (error) {
      console.log(error)
      return null
    }
  }
}
