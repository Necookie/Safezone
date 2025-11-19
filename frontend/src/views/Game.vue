<template>
  <div class="game-view">
    <!-- Back Button -->
    <div class="game-header">
      <button @click="goHome" class="back-btn">
        ← Back
      </button>
      <h1>{{ game.title }}</h1>
    </div>

    <!-- Game Container -->
    <div class="container">
      <div v-if="loading" class="loading-state">
        <p>Loading game...</p>
      </div>

      <div v-else-if="game.title && game.title !== 'Game not found'" class="game-grid">
        <!-- Game Frame -->
        <div class="game-frame">
          <div v-if="iframeError" class="error-message">
            <p>⚠️ Failed to load game</p>
            <p style="font-size: 0.9rem; color: #6B7280;">{{ iframeError }}</p>
            <button @click="openFullscreen" class="fullscreen-btn">
              Open in New Tab Instead
            </button>
          </div>
          <iframe 
            v-else
            :src="game.url" 
            class="iframe"
            allow="autoplay; fullscreen"
            title="Game"
            @error="handleIframeError"
            @load="handleIframeLoad"
          />
        </div>

        <!-- Sidebar -->
        <div class="sidebar">
          <!-- Info Card -->
          <div class="info-card">
            <h2>About This Game</h2>
            <p>{{ game.description }}</p>
          </div>

          <!-- Controls Card -->
          <div class="info-card">
            <h3>How to Play</h3>
            <p>{{ game.instructions }}</p>
          </div>

          <!-- Stats Card -->
          <div class="stats-card">
            <div class="stat">
              <span class="stat-label">Rating</span>
              <span class="stat-value">⭐ {{ game.rating }}</span>
            </div>
            <div class="stat">
              <span class="stat-label">Players</span>
              <span class="stat-value">👥 {{ game.players }}</span>
            </div>
          </div>

          <!-- Fullscreen Button -->
          <button @click="openFullscreen" class="fullscreen-btn">
            🖥️ Fullscreen
          </button>
        </div>
      </div>

      <div v-else class="error-state">
        <p>Game not found</p>
        <button @click="goHome" class="back-btn">Go Back Home</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const game = ref({ 
  title: '', 
  url: '', 
  instructions: '', 
  description: '', 
  rating: '0', 
  players: '0' 
})
const loading = ref(true)
const iframeError = ref(null)

onMounted(async () => {
  try {
    const gameId = parseInt(route.params.id)
    const response = await fetch('http://localhost:5000/api/games')
    
    if (response.ok) {
      const games = await response.json()
      const foundGame = games.find(g => g.id === gameId)
      
      if (foundGame) {
        game.value = foundGame
        console.log('Game loaded:', foundGame)
      } else {
        game.value = { 
          title: 'Game not found', 
          url: '', 
          instructions: '', 
          description: 'Please go back and select a valid game.', 
          rating: '0', 
          players: '0' 
        }
      }
    }
  } catch (error) {
    console.error('Error fetching games:', error)
    game.value = { 
      title: 'Error', 
      url: '', 
      instructions: '', 
      description: 'Failed to load game data.', 
      rating: '0', 
      players: '0' 
    }
  } finally {
    loading.value = false
  }
})

const goHome = () => {
  router.push('/')
}

const openFullscreen = () => {
  if (game.value.url) {
    window.open(game.value.url, '_blank')
  }
}

const handleIframeError = () => {
  iframeError.value = `Could not load: ${game.value.url}`
  console.error('Iframe load error')
}

const handleIframeLoad = () => {
  iframeError.value = null
  console.log('Iframe loaded successfully')
}
</script>

<style scoped>
.game-view {
  min-height: 100vh;
  background: linear-gradient(135deg, #F9FAFB 0%, var(--primary-light) 100%);
}

.game-header {
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  color: white;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(248, 117, 170, 0.2);
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.back-btn {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background: white;
  color: var(--primary);
  transform: translateX(-4px);
}

.game-header h1 {
  font-size: 2rem;
  margin: 0;
  flex: 1;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.loading-state,
.error-state {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--primary);
  font-size: 1.1rem;
}

.game-grid {
  display: grid;
  grid-template-columns: 1fr 350px;
  gap: 2rem;
}

.game-frame {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  position: relative;
}

.error-message {
  padding: 2rem;
  text-align: center;
  color: #DC2626;
}

.error-message p:first-child {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.iframe {
  width: 100%;
  height: 600px;
  border: none;
  display: block;
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-card {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.info-card h2 {
  font-size: 1.25rem;
  color: var(--primary);
  margin: 0 0 1rem 0;
}

.info-card h3 {
  font-size: 1rem;
  color: var(--dark);
  margin: 0 0 0.75rem 0;
}

.info-card p {
  color: #6B7280;
  line-height: 1.6;
  font-size: 0.9rem;
  margin: 0;
}

.stats-card {
  background: linear-gradient(135deg, var(--secondary) 0%, var(--accent) 100%);
  padding: 1.5rem;
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.stat {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stat-label {
  color: var(--dark);
  font-weight: 600;
  font-size: 0.9rem;
}

.stat-value {
  font-size: 1.25rem;
  font-weight: 700;
}

.fullscreen-btn {
  background: linear-gradient(135deg, var(--primary) 0%, #FF6B9D 100%);
  color: white;
  border: none;
  padding: 1rem;
  border-radius: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.fullscreen-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(248, 117, 170, 0.4);
}

@media (max-width: 1024px) {
  .game-grid {
    grid-template-columns: 1fr;
  }

  .sidebar {
    flex-direction: row;
    gap: 1rem;
  }

  .info-card {
    flex: 1;
  }
}

@media (max-width: 768px) {
  .game-header {
    flex-direction: column;
    text-align: center;
    padding: 1.5rem;
  }

  .game-header h1 {
    font-size: 1.5rem;
  }

  .back-btn {
    align-self: flex-start;
  }

  .container {
    padding: 1rem;
  }

  .iframe {
    height: 400px;
  }

  .sidebar {
    flex-direction: column;
    gap: 1rem;
  }

  .info-card,
  .stats-card {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .game-header h1 {
    font-size: 1.25rem;
  }

  .iframe {
    height: 300px;
  }

  .info-card h2 {
    font-size: 1rem;
  }

  .info-card p {
    font-size: 0.85rem;
  }
}
</style>
