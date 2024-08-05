import { Metadata } from 'next'
import { UserAuthForm } from './components/user-auth-form'
import Link from 'next/link'
import { buttonVariants } from '@/app/_components/ui/button'
import { cn } from '@/app/_lib/utils'

export const metadata: Metadata = {
  title: 'Authentication',
  description: 'Authentication forms built using the components.',
}

export default function AuthenticationPage() {
  return (
    <>
      <Link
        href={'/sign-up'}
        className={cn(
          buttonVariants({ variant: 'ghost' }),
          'absolute right-4 top-4 md:right-8 md:top-8',
        )}
      >
        Register
      </Link>
      <UserAuthForm />
    </>
  )
}
