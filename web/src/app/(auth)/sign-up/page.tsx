import { Metadata } from 'next'
import { UserAuthForm } from './components/user-auth-form'
import Link from 'next/link'
import { cn } from '@/app/_lib/utils'
import { buttonVariants } from '@/app/_components/ui/button'

export const metadata: Metadata = {
  title: 'Authentication',
  description: 'Authentication forms built using the components.',
}

export default function AuthenticationPage() {
  return (
    <>
      <Link
        href={'/sign-in'}
        className={cn(
          buttonVariants({ variant: 'ghost' }),
          'absolute right-4 top-4 md:right-8 md:top-8',
        )}
      >
        Login
      </Link>
      <UserAuthForm />
    </>
  )
}
