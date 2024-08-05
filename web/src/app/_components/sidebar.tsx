'use client'

import { Home, Clipboard } from 'lucide-react'
import Link from 'next/link'
import React, { cloneElement } from 'react'
import { usePathname } from 'next/navigation'
import { cn } from '../_lib/utils'

export function Sidebar() {
  const pathname = usePathname()

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

  const isActive = (path: string) => {
    return pathname === path
  }

  return (
    <div className="flex-1">
      <nav className="grid items-start px-2 text-sm font-medium lg:px-4">
        {sidebarItems.map((item) => (
          <Link
            key={item.path}
            href={item.path}
            className={cn(
              'flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground transition-all hover:text-primary',
              isActive(item.path) && 'bg-primary/10 text-primary',
            )}
          >
            {cloneElement(item.icon, {
              className: cn('h-4 w-4', isActive(item.path) && 'text-primary'),
            })}
            {item.label}
          </Link>
        ))}
        {/* <Link
          href="/"
          className="flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground transition-all hover:text-primary"
        >
          <Home className="h-4 w-4" />
          Dashboard
        </Link>
        <Link
          href="/reports"
          className={cn(
            'flex items-center gap-3 rounded-lg px-3 py-2 text-muted-foreground transition-all hover:text-primary',
            isActive('/reports') && 'bg-primary/10 text-primary',
          )}
        >
          <Clipboard className="h-4 w-4" />
          Reports
        </Link> */}
      </nav>
    </div>
  )
}
