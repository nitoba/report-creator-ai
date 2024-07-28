// middleware.ts
import { NextRequest, NextResponse } from 'next/server'
import { getSession } from './app/_lib/session'

const publicRoutes = ['/sign-in', '/sign-up']

export async function middleware(req: NextRequest) {
  const path = req.nextUrl.pathname
  const isProtectedRoute = !publicRoutes.includes(path)

  const session = await getSession()

  if (isProtectedRoute && !session.hasSession) {
    return NextResponse.redirect(new URL('/sign-in', req.nextUrl))
  }

  if (!isProtectedRoute && session.hasSession) {
    return NextResponse.redirect(new URL('/', req.nextUrl))
  }

  return NextResponse.next()
}

export const config = {
  matcher: [
    {
      source: '/((?!api|static|.*\\..*|_next|favicon.ico|robots.txt).*)',
      missing: [{ type: 'header', key: 'next-action' }],
    },
  ],
}
