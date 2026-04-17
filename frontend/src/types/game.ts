// src/types/game.ts

export type QuestionType =
  | 'single'
  | 'multiple'
  | 'boolean'
  | 'text'

export type AnswerValue =
  | number
  | number[]
  | string
  | null

export interface QuestionUI {
  id: string
  type: QuestionType
  text: string
  options?: string[]
}