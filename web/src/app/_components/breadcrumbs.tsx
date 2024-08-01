'use client'

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbSeparator,
} from './ui/breadcrumb'
import { usePathname } from 'next/navigation'

export function Breadcrumbs() {
  const pathname = usePathname()

  if (pathname === '/') {
    return null
  }

  const segments = window.location.pathname.split('/').filter(Boolean)

  return (
    <Breadcrumb>
      <BreadcrumbList>
        {segments.map((segment, index) => (
          <BreadcrumbItem key={segment}>
            <BreadcrumbLink href={`/${segment}`}>
              {segment[0].toUpperCase() + segment.substring(1)}
            </BreadcrumbLink>
            {index < segments.length - 1 && <BreadcrumbSeparator />}
          </BreadcrumbItem>
        ))}
      </BreadcrumbList>
    </Breadcrumb>
  )
}
