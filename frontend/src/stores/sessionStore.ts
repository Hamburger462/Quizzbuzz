// src/stores/sessionStore.ts

import { defineStore } from 'pinia'
import type { Player, Role, SessionStatus } from '../types'

interface SessionState {
  sessionId: string | null
  role: Role | null

  status: SessionStatus
  players: Player[]

  currentQuestionId: string | null
  questionIndex: number

  connected: boolean
  error: string | null
}

export const useSessionStore = defineStore('session', {
  state: (): SessionState => ({
    sessionId: null,
    role: null,
    status: 'idle',
    players: [],
    currentQuestionId: null,
    questionIndex: 0,
    connected: false,
    error: null
  }),

  actions: {
    setSession(sessionId: string, role: Role) {
      this.sessionId = sessionId
      this.role = role
    },

    updateFromRealtime(payload: Partial<SessionState>) {
      Object.assign(this, payload)
    },

    setConnection(status: boolean) {
      this.connected = status
    },

    reset() {
      this.$reset()
    }
  }
})