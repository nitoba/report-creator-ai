import {
  AuthenticatedUserResponse,
  AuthenticateUserBody,
} from '@/shared/dtos/authenticate-user-schema'
import { HttpClient } from '@/shared/http-client'

export class AuthenticateUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute({
    email,
    password,
  }: AuthenticateUserBody): Promise<AuthenticatedUserResponse> {
    const response = await this.httpClient.post('/auth/authenticate', {
      email,
      password,
    })

    if (response.status !== 201) {
      throw new Error(response.data.message)
    }

    return response.data
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
  }
}
