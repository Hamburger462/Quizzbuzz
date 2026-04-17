// src/stores/quizEditorStore.ts

import { defineStore } from 'pinia'
import type { QuestionDraft } from '../types'

interface QuizEditorState {
  currentQuizId: string | null
  title: string
  questions: QuestionDraft[]
  isDirty: boolean
  loading: boolean
  error: string | null
}

export const useQuizEditorStore = defineStore('quizEditor', {
  state: (): QuizEditorState => ({
    currentQuizId: null,
    title: '',
    questions: [],
    isDirty: false,
    loading: false,
    error: null
  }),

  actions: {
    setQuiz(data: { id: string; title: string; questions: QuestionDraft[] }) {
      this.currentQuizId = data.id
      this.title = data.title
      this.questions = data.questions
      this.isDirty = false
    },

    updateTitle(title: string) {
      this.title = title
      this.isDirty = true
    },

    addQuestion() {
      this.questions.push({
        id: null,
        text: '',
        options: [],
        correctAnswer: null,
        timeLimit: 30
      })
      this.isDirty = true
    },

    updateQuestion(index: number, question: QuestionDraft) {
      this.questions[index] = question
      this.isDirty = true
    },

    removeQuestion(index: number) {
      this.questions.splice(index, 1)
      this.isDirty = true
    },

    reset() {
      this.$reset()
    }
  }
})