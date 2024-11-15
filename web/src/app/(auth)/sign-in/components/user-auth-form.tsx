'use client'

import { Button } from '@/app/_components/ui/button'
import { Input } from '@/app/_components/ui/input'
import { cn } from '@/app/_lib/utils'

import { Loader2, Stars } from 'lucide-react'
import { zodResolver } from '@hookform/resolvers/zod'
import { useForm } from 'react-hook-form'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/app/_components/ui/form'
import {
  AuthenticateUserBody,
  authenticateUserSchema,
} from '@/shared/dtos/authenticate-user-schema'
import { useServerAction } from 'zsa-react'
import { useRouter } from 'next/navigation'
import { authenticateUserAction } from '@/app/_actions/authenticate-user-action'
import { toast } from 'sonner'

interface UserAuthFormProps extends React.HTMLAttributes<HTMLDivElement> {}

export function UserAuthForm({ className, ...props }: UserAuthFormProps) {
  const { replace } = useRouter()
  const { execute, isPending } = useServerAction(authenticateUserAction, {
    onError: (error) => {
      toast.error(error.err.data)
    },
    onSuccess: (result) => {
      if (!result.data) {
        toast.error('Invalid credentials')
        return
      }
      console.log('Resultado:', result)
      localStorage.setItem('access_token', result.data.access_token)
      toast.success('Account authenticated successfully')
      replace('/')
    },
  })
  const form = useForm<AuthenticateUserBody>({
    resolver: zodResolver(authenticateUserSchema),
  })

  function onSubmit(values: AuthenticateUserBody) {
    execute(values)
  }
  return (
    <div
      className={cn('grid gap-6 animate-in fade-in-50 duration-300', className)}
      {...props}
    >
      <div className="flex flex-col space-y-2 text-center items-center">
        <div className="flex flex-col gap-1 items-center text-3xl font-medium font-mono mb-5 sm:hidden">
          <Stars className="size-8 mr-2" />
          Report Creator AI
        </div>
        <h1 className="text-2xl font-semibold tracking-tight">
          Login into your account
        </h1>
        <p className="text-sm text-muted-foreground">
          Enter your with your credentials below to login into your account
        </p>
      </div>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="grid gap-3">
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input
                    type="email"
                    autoCapitalize="none"
                    autoComplete="email"
                    autoCorrect="off"
                    placeholder="name@example.com"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input placeholder="*****" type="password" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">
            {isPending && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Sign In
          </Button>
        </form>
      </Form>
    </div>
  )
}
