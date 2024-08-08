'use client'

import { MoreHorizontal } from 'lucide-react'

import { Badge } from '@/app/_components/ui/badge'
import { Button } from '@/app/_components/ui/button'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from '@/app/_components/ui/dropdown-menu'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/app/_components/ui/table'
import { Card, CardContent, CardFooter } from '@/app/_components/ui/card'
import { fetchReportsFromUserAction } from '@/app/_actions/fetch-reports-from-user-action'
import { useServerActionQuery } from '@/app/_hooks/useServerActionHooks'
import dayjs from 'dayjs'
import { Pagination } from '@/app/_components/ui/pagination'
import { ReportsTableSkeleton } from './reports-skeleton'
import { useQueryState, parseAsInteger } from 'nuqs'
export function ReportsList() {
  const [page, setPage] = useQueryState('page', parseAsInteger.withDefault(1))

  const { data: reports, isLoading } = useServerActionQuery(
    fetchReportsFromUserAction,
    {
      input: {
        page_index: page - 1,
        page_size: 10,
      },
      queryKey: ['reports', page],
    },
  )

  function handlePaginate(page: number) {
    setPage(page + 1)
  }

  return (
    <Card className="rounded-lg border border-dashed shadow-sm">
      <CardContent className="sm:mt-4 p-2 sm:p-6 mt-0">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Title</TableHead>
              <TableHead>Word Count</TableHead>
              <TableHead className="hidden md:table-cell">Created at</TableHead>
              <TableHead>
                <span className="sr-only">Actions</span>
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {isLoading && <ReportsTableSkeleton />}
            {reports?.data.map((report) => (
              <TableRow key={report.id}>
                <TableCell className="font-medium">{report.title}</TableCell>
                <TableCell>
                  <Badge variant="outline">{report.word_count}</Badge>
                </TableCell>
                <TableCell className="hidden md:table-cell">
                  {dayjs(report.created_at).format('DD/MM/YYYY [at] HH:mm:ss')}
                </TableCell>
                <TableCell>
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button aria-haspopup="true" size="icon" variant="ghost">
                        <MoreHorizontal className="h-4 w-4" />
                        <span className="sr-only">Toggle menu</span>
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                      <DropdownMenuLabel>Actions</DropdownMenuLabel>
                      <DropdownMenuItem>Edit</DropdownMenuItem>
                      <DropdownMenuItem>Delete</DropdownMenuItem>
                    </DropdownMenuContent>
                  </DropdownMenu>
                </TableCell>
              </TableRow>
            ))}
            {reports?.data && reports.data.length === 0 && (
              <TableRow>
                <TableCell colSpan={4} className="text-center pt-24">
                  No reports found.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </CardContent>
      <CardFooter className="p-2 sm:p-6">
        {reports?.data && reports.data.length > 0 && (
          <Pagination
            pageIndex={reports.page}
            perPage={reports.size}
            totalCount={reports.total}
            onPageChange={handlePaginate}
          />
        )}
      </CardFooter>
    </Card>
  )
}
