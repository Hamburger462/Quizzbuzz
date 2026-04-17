<!-- src/components/game/SingleChoice.vue -->
<template>
  <div class="options">
    <button
      v-for="(option, index) in options"
      :key="index"
      :class="['option', { selected: modelValue === index }]"
      :disabled="disabled"
      @click="select(index)"
    >
      {{ option }}
    </button>
  </div>
</template>

<script setup lang="ts">
interface Props {
  options: string[]
  modelValue: number | null
  disabled?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: number): void
  (e: 'answered'): void
}>()

function select(index: number) {
  if (props.disabled) return

  emit('update:modelValue', index)
  emit('answered')
}
</script>

<style scoped>
.options {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.option {
  padding: 16px;
  border: 1px solid #ccc;
  cursor: pointer;
}

.option.selected {
  background: #3b82f6;
  color: white;
}
</style>