<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>Welcome to Safezone</h1>
        <p>Discover and play amazing games</p>
      </div>
    </section>

    <!-- Games Section -->
    <section class="games-section">
      <div class="container">
        <h2>Featured Games</h2>
        
        <div v-if="loading" class="loading">
          <p>Loading games...</p>
        </div>

        <div v-else-if="games.length > 0" class="games-grid">
          <GameCard
            v-for="game in games"
            :key="game.id"
            :title="game.title"
            :description="game.description"
            :rating="game.rating"
            :players="game.players"
            @click="goToGame(game.id)"
          />
        </div>

        <div v-else class="empty-state">
          <p>No games available yet. Check back soon!</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import GameCard from '../components/ui/GameCard.vue'

const router = useRouter()
const games = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/api/games')
    if (response.ok) {
      games.value = await response.json()
    } else {
      console.error('Failed to fetch games')
    }
  } catch (error) {
    console.error('Error fetching games:', error)
  } finally {
    loading.value = false
  }
})

const goToGame = (gameId) => {
  router.push(`/game/${gameId}`)
}
</script>

<style scoped>
.home {
  min-height: 100vh;
  background: linear-gradient(135deg, #F9FAFB 0%, var(--primary-light) 100%);
}

.hero {
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  color: white;
  padding: 6rem 2rem;
  text-align: center;
  box-shadow: 0 8px 24px rgba(248, 117, 170, 0.2);
}

.hero-content h1 {
  font-size: 3rem;
  margin: 0 0 1rem 0;
  font-weight: 800;
}

.hero-content p {
  font-size: 1.25rem;
  margin: 0;
  opacity: 0.95;
}

.games-section {
  padding: 4rem 2rem;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
}

.games-section h2 {
  font-size: 2rem;
  color: var(--dark);
  margin-bottom: 3rem;
  text-align: center;
}

.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.loading {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--primary);
  font-size: 1.1rem;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #9CA3AF;
}

@media (max-width: 768px) {
  .hero {
    padding: 4rem 1rem;
  }

  .hero-content h1 {
    font-size: 2rem;
  }

  .hero-content p {
    font-size: 1rem;
  }

  .games-section {
    padding: 2rem 1rem;
  }

  .games-section h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }

  .games-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (max-width: 480px) {
  .hero {
    padding: 3rem 1rem;
  }

  .hero-content h1 {
    font-size: 1.5rem;
  }
}
</style>
