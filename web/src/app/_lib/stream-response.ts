export type IterableStreamResponse = {
  data: string
  isDone: boolean
}

export async function* getIterableStream(
  body: ReadableStream<Uint8Array>,
): AsyncIterable<IterableStreamResponse> {
  const reader = body.getReader()
  const decoder = new TextDecoder()

  while (true) {
    const { value, done } = await reader.read()
    if (done) {
      yield { data: '', isDone: true }
      break
    }
    const decodedChunk = decoder.decode(value, { stream: true })
    yield { data: decodedChunk, isDone: false }
  }
}
