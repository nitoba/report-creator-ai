import { RegisterUserBody } from '@/shared/dtos/register-user-schema'
import { HttpClient } from '@/shared/http-client'

export class RegisterUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute({ username, email, password }: RegisterUserBody) {
    const response = await this.httpClient.post('/auth/register', {
      username,
      email,
      password,
    })

    if (response.status !== 201) {
      throw new Error(response.data.message)
    }
  }
}
