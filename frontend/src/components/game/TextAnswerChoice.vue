<!-- src/components/game/TextAnswer.vue -->
<template>
  <input
    type="text"
    :value="modelValue ?? ''"
    :disabled="disabled"
    @input="onInput"
    @blur="emitAnswered"
  />
</template>

<script setup lang="ts">
interface Props {
  modelValue: string | null
  disabled?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
  (e: 'answered'): void
}>()

function onInput(e: Event) {
  const value = (e.target as HTMLInputElement).value
  emit('update:modelValue', value)
}

function emitAnswered() {
  emit('answered')
}
</script>