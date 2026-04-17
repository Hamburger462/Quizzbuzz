<!-- src/layouts/AppLayout.vue -->
<template>
  <div class="app-layout">
    <AppHeader />

    <main class="app-content">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import AppHeader from './Header.vue'
</script>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.app-content {
  flex: 1;
  padding: 24px;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}
</style>