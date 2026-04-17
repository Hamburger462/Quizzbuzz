// src/stores/gameStore.ts

import { defineStore } from 'pinia'

interface GameState {
  selectedAnswer: number | null
  hasAnswered: boolean

  timeLeft: number
  questionStartTime: number | null

  showResults: boolean
  correctAnswer: number | null

  loading: boolean
}

export const useGameStore = defineStore('game', {
  state: (): GameState => ({
    selectedAnswer: null,
    hasAnswered: false,
    timeLeft: 0,
    questionStartTime: null,
    showResults: false,
    correctAnswer: null,
    loading: false
  }),

  actions: {
    selectAnswer(index: number) {
      if (this.hasAnswered) return

      this.selectedAnswer = index
      this.hasAnswered = true
    },

    setTimer(timeLeft: number, startTime: number) {
      this.timeLeft = timeLeft
      this.questionStartTime = startTime
    },

    showAnswerResults(correctAnswer: number) {
      this.correctAnswer = correctAnswer
      this.showResults = true
    },

    resetQuestionState() {
      this.selectedAnswer = null
      this.hasAnswered = false
      this.showResults = false
      this.correctAnswer = null
    }
  }
})