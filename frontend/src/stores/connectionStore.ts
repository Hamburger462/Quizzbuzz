// src/stores/connectionStore.ts

import { defineStore } from 'pinia'

interface ConnectionState {
  firebaseConnected: boolean
  reconnecting: boolean
  lastSyncTime: number | null
  latency: number | null
}

export const useConnectionStore = defineStore('connection', {
  state: (): ConnectionState => ({
    firebaseConnected: false,
    reconnecting: false,
    lastSyncTime: null,
    latency: null
  }),

  actions: {
    setConnected(status: boolean) {
      this.firebaseConnected = status
    },

    setReconnecting(status: boolean) {
      this.reconnecting = status
    },

    updateSyncTime() {
      this.lastSyncTime = Date.now()
    },

    setLatency(latency: number) {
      this.latency = latency
    }
  }
})