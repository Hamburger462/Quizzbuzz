<!-- src/components/game/MultipleChoice.vue -->
<template>
  <div class="options">
    <button
      v-for="(option, index) in options"
      :key="index"
      :class="['option', { selected: isSelected(index) }]"
      :disabled="disabled"
      @click="toggle(index)"
    >
      {{ option }}
    </button>
  </div>
</template>

<script setup lang="ts">
interface Props {
  options: string[]
  modelValue: number[]
  disabled?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: number[]): void
  (e: 'answered'): void
}>()

function isSelected(index: number) {
  return props.modelValue.includes(index)
}

function toggle(index: number) {
  if (props.disabled) return

  const next = [...props.modelValue]

  const i = next.indexOf(index)
  if (i >= 0) {
    next.splice(i, 1)
  } else {
    next.push(index)
  }

  emit('update:modelValue', next)
  emit('answered')
}
</script>