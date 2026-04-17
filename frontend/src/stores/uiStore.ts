// src/stores/uiStore.ts

import { defineStore } from 'pinia'

interface Notification {
  id: string
  message: string
  type: 'success' | 'error' | 'info'
}

interface UIState {
  isLoading: boolean
  globalError: string | null
  notifications: Notification[]

  modals: {
    createQuiz: boolean
    joinSession: boolean
  }
}

export const useUIStore = defineStore('ui', {
  state: (): UIState => ({
    isLoading: false,
    globalError: null,
    notifications: [],
    modals: {
      createQuiz: false,
      joinSession: false
    }
  }),

  actions: {
    setLoading(value: boolean) {
      this.isLoading = value
    },

    setError(error: string | null) {
      this.globalError = error
    },

    addNotification(notification: Notification) {
      this.notifications.push(notification)
    },

    removeNotification(id: string) {
      this.notifications = this.notifications.filter(n => n.id !== id)
    },

    toggleModal(name: keyof UIState['modals'], value: boolean) {
      this.modals[name] = value
    }
  }
})