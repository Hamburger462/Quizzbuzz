// src/stores/authStore.ts

import { defineStore } from 'pinia'

interface AuthState {
  user: unknown | null // Firebase User (type later if needed)
  token: string | null
  isAuthenticated: boolean
  loading: boolean
  error: string | null
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    user: null,
    token: null,
    isAuthenticated: false,
    loading: false,
    error: null
  }),

  actions: {
    setAuth(user: unknown, token: string) {
      this.user = user
      this.token = token
      this.isAuthenticated = true
    },

    clearAuth() {
      this.$reset()
    },

    setLoading(value: boolean) {
      this.loading = value
    },

    setError(error: string | null) {
      this.error = error
    }
  }
})