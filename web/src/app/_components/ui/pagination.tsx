import {
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
} from 'lucide-react'
import { Button } from './button'

type Props = {
  pageIndex: number
  totalCount: number
  perPage: number
  onPageChange: (pageIndex: number) => void
}

export function Pagination({
  pageIndex,
  totalCount,
  perPage,
  onPageChange,
}: Props) {
  const pages = Math.ceil(totalCount / perPage) || 1
  const canGoToNextPage = pageIndex + 1 < pages
  const canGoToPrevPage = pageIndex - 1 >= 0

  return (
    <div className="flex items-center justify-between w-full">
      <span className="text-sm text-muted-foreground">
        Total of the {totalCount} items(s)
      </span>

      <div className="flex items-center gap-6 lg:gap-8">
        <span className="text-sm font-medium">
          Page {pageIndex + 1} from {pages}
        </span>

        <div className="flex items-center gap-2">
          <Button
            variant="outline"
            className="size-8 p-0"
            disabled={pageIndex === 0}
            onClick={() => onPageChange(0)}
          >
            <ChevronsLeft className="size-4" />
            <span className="sr-only">Primeira página</span>
          </Button>

          <Button
            variant="outline"
            className="size-8 p-0"
            disabled={!canGoToPrevPage}
            onClick={() => onPageChange(pageIndex - 1)}
          >
            <ChevronLeft className="size-4" />
            <span className="sr-only">Página anterior</span>
          </Button>

          <Button
            variant="outline"
            className="size-8 p-0"
            disabled={!canGoToNextPage}
            onClick={() => onPageChange(pageIndex + 1)}
          >
            <ChevronRight className="size-4" />
            <span className="sr-only">Próxima página</span>
          </Button>

          <Button
            variant="outline"
            className="size-8 p-0"
            disabled={pages - 1 <= pageIndex}
            onClick={() => onPageChange(pages - 1)}
          >
            <ChevronsRight className="size-4" />
            <span className="sr-only">Última página</span>
          </Button>
        </div>
      </div>
    </div>
  )
}
