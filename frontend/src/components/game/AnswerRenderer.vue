<!-- AnswerRenderer.vue -->
<template>
  <SingleChoice
    v-if="question.type === 'single'"
    v-model="singleValue"
    :options="question.options!"
    :disabled="disabled"
    @answered="handleAnswered"
  />

  <MultipleChoice
    v-else-if="question.type === 'multiple'"
    v-model="multipleValue"
    :options="question.options!"
    :disabled="disabled"
    @answered="handleAnswered"
  />

  <BooleanChoice
    v-else-if="question.type === 'boolean'"
    v-model="singleValue"
    :disabled="disabled"
    @answered="handleAnswered"
  />

  <TextAnswer
    v-else-if="question.type === 'text'"
    v-model="textValue"
    :disabled="disabled"
    @answered="handleAnswered"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { QuestionUI, AnswerValue } from '../../types/game'

import SingleChoice from './SingleChoice.vue'
import MultipleChoice from './MultipleChoice.vue'
import BooleanChoice from './BooleanChoice.vue'
import TextAnswer from './TextAnswerChoice.vue'

interface Props {
  question: QuestionUI
  disabled?: boolean
}

const props = defineProps<Props>()

const emit = defineEmits<{
  (e: 'answer', value: AnswerValue): void
  (e: 'answered'): void
}>()

// 🔑 TYPE-SAFE computed bindings

const singleValue = computed<number | null>({
  get: () => props.question.type === 'single' || props.question.type === 'boolean'
    ? (currentValue.value as number | null)
    : null,
  set: (val) => emitAnswer(val)
})

const multipleValue = computed<number[]>({
  get: () => props.question.type === 'multiple'
    ? (currentValue.value as number[]) ?? []
    : [],
  set: (val) => emitAnswer(val)
})

const textValue = computed<string>({
  get: () => props.question.type === 'text'
    ? (currentValue.value as string) ?? ''
    : '',
  set: (val) => emitAnswer(val)
})

// internal value
const currentValue = computed<AnswerValue | null>(() => null)

function emitAnswer(value: AnswerValue) {
  emit('answer', value)
}

function handleAnswered() {
  emit('answered')
}
</script>