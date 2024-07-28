import {
  AuthenticatedUserResponse,
  AuthenticateUserBody,
} from '@/shared/dtos/authenticate-user-schema'
import { HttpClient } from '@/shared/http-client'

export class AuthenticateUserService {
  constructor(private readonly httpClient: HttpClient) {}

  async execute({ email, password }: AuthenticateUserBody) {
    try {
      const response = await this.httpClient.post<AuthenticatedUserResponse>(
        '/auth/authenticate',
        { email, password },
      )

      return response.data
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      console.log('ERROR NO SERVICE', error.response?.data)
      throw new Error(error.response?.data)
    }
  }
}
