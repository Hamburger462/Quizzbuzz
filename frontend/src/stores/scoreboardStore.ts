// src/stores/scoreboardStore.ts

import { defineStore } from 'pinia'
import type { ScoreEntry } from '../types'

interface ScoreboardState {
  scores: ScoreEntry[]
  lastUpdated: number | null
  loading: boolean
}

export const useScoreboardStore = defineStore('scoreboard', {
  state: (): ScoreboardState => ({
    scores: [],
    lastUpdated: null,
    loading: false
  }),

  actions: {
    setScores(scores: ScoreEntry[]) {
      this.scores = scores
      this.lastUpdated = Date.now()
    },

    reset() {
      this.$reset()
    }
  }
})