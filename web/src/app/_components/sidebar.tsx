'use client'

import { Home, Clipboard } from 'lucide-react'
import Link from 'next/link'
import React, { cloneElement } from 'react'
import { usePathname } from 'next/navigation'
import { cn } from '../_lib/utils'
import { SheetClose } from './ui/sheet'

export type SidebarItem = {
  isInSheet?: boolean
}

const sidebarItems = [
  {
    label: 'Dashboard',
    path: '/',
    icon: <Home className="h-4 w-4" />,
  },
  {
    label: 'Reports',
    path: '/reports',
    icon: <Clipboard className="h-4 w-4" />,
  },
]

function RenderLinks({
  icon,
  label,
  path,
  isActive,
  isInSheet,
}: (typeof sidebarItems)[number] & {
  isActive: (path: string) => boolean
  isInSheet: boolean
}) {
  if (isInSheet) {
    return (
      <SheetClose asChild>
        <Link
          href={path}
          className={cn(
            'flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground transition-all hover:text-primary',
            isActive(path) && 'bg-primary/10 text-primary',
          )}
        >
          {cloneElement(icon, {
            className: cn('h-4 w-4', isActive(path) && 'text-primary'),
          })}
          {label}
        </Link>
      </SheetClose>
    )
  }

  return (
    <Link
      href={path}
      className={cn(
        'flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground transition-all hover:text-primary',
        isActive(path) && 'bg-primary/10 text-primary',
      )}
    >
      {cloneElement(icon, {
        className: cn('h-4 w-4', isActive(path) && 'text-primary'),
      })}
      {label}
    </Link>
  )
}

export function Sidebar({ isInSheet = false }: SidebarItem) {
  const pathname = usePathname()

  const isActive = (path: string) => {
    return pathname === path
  }

  return (
    <div className="flex-1">
      <nav className="grid items-start text-sm font-medium lg:px-4">
        {sidebarItems.map((item) => (
          <RenderLinks
            key={item.path}
            {...item}
            isActive={isActive}
            isInSheet={isInSheet}
          />
        ))}
      </nav>
    </div>
  )
}
