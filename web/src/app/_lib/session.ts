import 'server-only'

import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

type SessionPayload = {
  sub: string
  username: string
  email: string
  exp: number
}
function createExpiresAt() {
  const days = 30 * 24 * 60 * 60 * 1000 // 30 days
  const expiresAt = new Date(Date.now() + days)
  return expiresAt
}

function parseJwt(token: string) {
  try {
    return JSON.parse(atob(token.split('.')[1])) as SessionPayload
  } catch (e) {
    return null
  }
}
export async function createSession(token: string) {
  const expiresAt = createExpiresAt()

  cookies().set('session', token, {
    httpOnly: true,
    secure: false,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}

export async function getSession() {
  const cookie = cookies().get('session')?.value

  if (!cookie) {
    const left: {
      hasSession: false
      sub?: undefined
      username?: undefined
      email?: undefined
    } = { hasSession: false }

    return left
  }

  const session = parseJwt(cookie)

  if (!!session && !!session.sub) {
    const exp = session.exp * 1000

    const now = Date.now()

    if (exp < now) {
      const left: {
        hasSession: false
        sub?: undefined
        username?: undefined
        email?: undefined
      } = { hasSession: false }
      return left
    }

    const right: {
      hasSession: true
      sub: string
      username: string
      email: string
    } = {
      hasSession: true,
      sub: session.sub,
      username: session.username,
      email: session.email,
    }
    return right
  } else {
    const left: {
      hasSession: false
      sub?: undefined
      username?: undefined
      email?: undefined
    } = { hasSession: false }
    return left
  }
}

export async function updateSessionMiddleware(
  sessionPayload: SessionPayload,
  res?: NextResponse,
) {
  const response = res || NextResponse.next()
  const expiresAt = createExpiresAt()
  const token = 'await createToken(sessionPayload, expiresAt)'
  response.cookies.set({
    name: 'session',
    value: token,
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'strict',
    path: '/',
  })
  return response
}

export async function getRawSession() {
  const cookie = cookies().get('session')?.value
  if (!cookie) {
    return null
  }
  return cookie
}

export function deleteSession() {
  cookies().set('session', '', { expires: new Date(0) })
}
