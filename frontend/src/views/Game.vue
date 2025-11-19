<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <div class="max-w-6xl mx-auto">
      <!-- Back Button -->
      <button 
        @click="goHome"
        class="mb-6 flex items-center text-blue-600 hover:text-blue-800 font-semibold"
      >
        ← Back to Games
      </button>

      <!-- Game Header -->
      <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">{{ game.title }}</h1>
        <div class="flex gap-6 text-gray-600">
          <span>⭐ {{ game.rating }} rating</span>
          <span>👥 {{ game.players }} players</span>
        </div>
      </div>

      <!-- Main Content Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Game Frame (Main) -->
        <div class="lg:col-span-2">
          <div class="bg-white rounded-lg shadow-lg overflow-hidden">
            <iframe 
              :src="game.url" 
              class="w-full h-[500px] md:h-[600px] border-0"
              allow="autoplay; fullscreen"
              title="Game"
            />
          </div>
        </div>

        <!-- Sidebar (Description & Info) -->
        <div class="lg:col-span-1">
          <!-- Info Card -->
          <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h2 class="text-xl font-bold text-gray-800 mb-4">About</h2>
            <p class="text-gray-700 leading-relaxed mb-4">
              {{ game.description }}
            </p>
            
            <div class="border-t pt-4">
              <h3 class="font-semibold text-gray-800 mb-3">Controls</h3>
              <p class="text-gray-600 text-sm">
                {{ game.instructions }}
              </p>
            </div>
          </div>

          <!-- Fullscreen Button -->
          <button 
            @click="openFullscreen"
            class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white py-3 rounded-lg font-semibold hover:from-blue-600 hover:to-indigo-700 transition"
          >
            🖥️ Fullscreen
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const game = ref({ title: '', url: '', instructions: '', description: '', rating: '0', players: '0' })

const gamesData = [
  {
    id: 1,
    title: 'Hill Racing 43',
    description: 'An exciting racing game where you drive your car up challenging hills. Navigate through obstacles, collect power-ups, and complete all levels. Perfect for testing your driving skills!',
    url: 'http://127.0.0.1:5000/static/games/hill-racing-43/index.html',
    instructions: 'Use Arrow Keys or WASD to drive. Press Space to jump. Complete all levels to win!',
    rating: '4.5',
    players: '1,234'
  },
  {
    id: 2,
    title: 'Cute Pong',
    description: 'A modern twist on the classic Pong game. Rally against an intelligent AI opponent in this addictive game of reflexes and strategy. Simple to learn, hard to master!',
    url: 'http://127.0.0.1:5000/static/games/cute-pong/index.html',
    instructions: 'Use Mouse or Touch to control the paddle. Keep the ball in play and outscore your opponent!',
    rating: '4.8',
    players: '2,456'
  }
]

onMounted(() => {
  const id = parseInt(route.params.id)
  const foundGame = gamesData.find(g => g.id === id)
  if (foundGame) {
    game.value = foundGame
  } else {
    game.value = { title: 'Game not found', url: '', instructions: '', description: '', rating: '0', players: '0' }
  }
})

const goHome = () => {
  router.push('/')
}

const openFullscreen = () => {
  window.open(game.value.url, '_blank')
}
</script>
