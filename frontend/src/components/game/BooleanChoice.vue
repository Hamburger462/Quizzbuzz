<!-- src/components/game/BooleanChoice.vue -->
<template>
  <div class="boolean">
    <button
      :class="{ selected: modelValue === 1 }"
      @click="select(1)"
    >
      True
    </button>

    <button
      :class="{ selected: modelValue === 0 }"
      @click="select(0)"
    >
      False
    </button>
  </div>
</template>

<script setup lang="ts">
interface Props {
  modelValue: number | null
  disabled?: boolean
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: number): void
  (e: 'answered'): void
}>()

function select(value: number) {
  if (props.disabled) return

  emit('update:modelValue', value)
  emit('answered')
}
</script>