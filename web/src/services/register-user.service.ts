import { RegisterUserBody } from '@/shared/dtos/register-user-schema'
import { HttpClient } from '@/shared/http-client'

export class RegisterUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute({ username, email, password }: RegisterUserBody) {
    try {
      await this.httpClient.post('/auth/register', {
        username,
        email,
        password,
      })

      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log('ERROR NO SERVICE', error.response?.data)
      throw new Error(error.response?.data)
    }
  }
}
