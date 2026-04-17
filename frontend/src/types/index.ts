// src/types/index.ts

export type Role = 'host' | 'player'

export type SessionStatus =
  | 'idle'
  | 'lobby'
  | 'question'
  | 'scoreboard'
  | 'finished'

export interface Player {
  id: string
  name: string
  score: number
}

export interface QuestionDraft {
  id: string | null
  text: string
  options: string[]
  correctAnswer: number | null
  timeLimit: number
}

export interface ScoreEntry {
  userId: string
  name: string
  score: number
  rank: number
}