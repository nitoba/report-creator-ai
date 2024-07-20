export class ServiceLocator {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private static _cache: Record<string, any>

  static {
    console.log('Setting up cache')
    ServiceLocator._cache = {}
  }

  static get<T>(key: string): T {
    if (key in this._cache) {
      return this._cache[key]
    }

    const service = this._cache[key]

    if (!service) {
      throw new Error(`Service ${key} not found`)
    }

    return service
  }

  static set<T>(key: string, value: T): void {
    if (this._cache[key]) return
    this._cache[key] = value
  }
}
