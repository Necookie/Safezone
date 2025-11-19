<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-800 mb-2">Safezone</h1>
        <p class="text-lg text-gray-600">Play amazing games online</p>
      </div>

      <!-- Games Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="game in gamesData" 
          :key="game.id"
          @click="goToGame(game.id)"
          class="cursor-pointer transform transition hover:scale-105"
        >
          <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-2xl">
            <!-- Game Card Image/Icon -->
            <div class="h-48 bg-gradient-to-br from-blue-400 to-indigo-600 flex items-center justify-center">
              <span class="text-6xl">🎮</span>
            </div>

            <!-- Card Content -->
            <div class="p-6">
              <h2 class="text-2xl font-bold text-gray-800 mb-2">{{ game.title }}</h2>
              <p class="text-gray-600 mb-4 line-clamp-2">{{ game.description }}</p>
              
              <!-- Game Stats -->
              <div class="flex justify-between text-sm text-gray-500 mb-4">
                <span>⭐ {{ game.rating }}</span>
                <span>👥 {{ game.players }} players</span>
              </div>

              <!-- Play Button -->
              <button 
                class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white py-2 rounded-lg font-semibold hover:from-blue-600 hover:to-indigo-700 transition"
              >
                Play Now
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="gamesData.length === 0" class="text-center py-12">
        <p class="text-gray-500 text-lg">No games available yet. Check back soon!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const gamesData = ref([
  {
    id: 1,
    title: 'Hill Racing 43',
    description: 'Drive your car up hills and complete challenging levels. Use arrow keys to navigate through obstacles.',
    url: 'http://127.0.0.1:5000/static/games/hill-racing-43/index.html',
    instructions: 'Use arrow keys to drive your car up hills and complete the levels.',
    rating: '4.5',
    players: '1,234'
  },
  {
    id: 2,
    title: 'Cute Pong',
    description: 'Classic pong game with a cute twist. Play against the AI and test your reflexes.',
    url: 'http://127.0.0.1:5000/static/games/cute-pong/index.html',
    instructions: 'Use mouse or touch to control the paddle and hit the ball.',
    rating: '4.8',
    players: '2,456'
  }
])

const goToGame = (gameId) => {
  router.push(`/game/${gameId}`)
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
