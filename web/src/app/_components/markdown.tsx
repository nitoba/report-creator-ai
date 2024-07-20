import React from 'react'
import Markdown from 'react-markdown'

export function ContentMarkdown({ content }: { content: string }) {
  return (
    <Markdown
      className="prose prose-sm max-w-none rounded-md bg-muted p-4 h-full max-h-[calc(60vh)] overflow-y-scroll w-full"
      components={{
        pre: ({ children }) => (
          <pre className="bg-muted rounded-md p-4 overflow-x-auto">
            {children}
          </pre>
        ),
        code: ({ ...props }) => (
          <code className="bg-muted rounded-md p-1" {...props} />
        ),
      }}
    >
      {content}
    </Markdown>
  )
}
