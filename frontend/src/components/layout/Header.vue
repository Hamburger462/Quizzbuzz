<!-- src/components/layout/AppHeader.vue -->
<template>
  <header class="header">
    <div class="header-container">
      <!-- Left: Logo -->
      <div class="logo" @click="goHome">
        QuizApp
      </div>

      <!-- Center: Navigation -->
      <nav class="nav">
        <button @click="goToDashboard">Dashboard</button>
        <button @click="openJoinModal">Join</button>
      </nav>

      <!-- Right: Auth / Session -->
      <div class="actions">
        <span v-if="isAuthenticated" class="user">
          {{ userDisplay }}
        </span>

        <button v-if="!isAuthenticated" @click="goToLogin">
          Login
        </button>

        <button v-else @click="logout">
          Logout
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/authStore'
import { useUIStore } from '../../stores/uiStore'

const router = useRouter()
const authStore = useAuthStore()
const uiStore = useUIStore()

const isAuthenticated = computed(() => authStore.isAuthenticated)

const userDisplay = computed(() => {
  // adjust once you type Firebase user properly
  return 'User'
})

function goHome() {
  router.push('/')
}

function goToDashboard() {
  router.push('/dashboard')
}

function goToLogin() {
  router.push('/login')
}

function openJoinModal() {
  uiStore.toggleModal('joinSession', true)
}

function logout() {
  authStore.clearAuth()
  router.push('/login')
}
</script>

<style scoped>
.header {
  height: 64px;
  border-bottom: 1px solid #e5e7eb;
  background: white;
  display: flex;
  align-items: center;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  padding: 0 24px;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  font-weight: bold;
  font-size: 18px;
  cursor: pointer;
}

.nav {
  display: flex;
  gap: 16px;
}

.nav button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 14px;
}

.actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.actions button {
  padding: 6px 12px;
  cursor: pointer;
}

.user {
  font-size: 14px;
  color: #555;
}
</style>