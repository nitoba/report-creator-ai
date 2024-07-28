import 'server-only'
import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

type SessionPayload = {
  sub: string
  email: string
}
function createExpiresAt() {
  const days = 30 * 24 * 60 * 60 * 1000 // time in milliseconds
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
export async function createSession() {
  const expiresAt = createExpiresAt()
  const token = 'await createToken(sessionPayload, expiresAt)'

  cookies().set('session', token, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'strict',
    path: '/',
  })
}

export async function getSession() {
  const cookie = cookies().get('session')?.value

  if (!cookie) {
    const left: {
      hasSession: false
      sub?: undefined
      email?: undefined
    } = { hasSession: false }

    return left
  }
  const session = parseJwt(cookie)
  if (!!session && !!session.sub) {
    const right: {
      hasSession: true
      sub: string
      email: string
    } = {
      hasSession: true,
      sub: session.sub,
      email: session.email,
    }
    return right
  } else {
    const left: {
      hasSession: false
      sub?: undefined
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

export function deleteSession() {
  cookies().delete('session')
}