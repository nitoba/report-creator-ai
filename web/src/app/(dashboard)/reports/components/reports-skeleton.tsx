import { Button } from '@/app/_components/ui/button'
import { Skeleton } from '@/app/_components/ui/skeleton'
import { TableCell, TableRow } from '@/app/_components/ui/table'
import { Search } from 'lucide-react'

export function ReportsTableSkeleton() {
  return Array.from({ length: 10 }).map((_, i) => (
    <TableRow key={i}>
      <TableCell>
        <Button variant="outline" size="xs" disabled>
          <Search className="size-3" />
          <span className="sr-only">Detalhes do pedido</span>
        </Button>
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[175px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[148px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[110px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[200px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[64px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[92px]" />
      </TableCell>
      <TableCell>
        <Skeleton className="h-4 w-[92px]" />
      </TableCell>
    </TableRow>
  ))
}
