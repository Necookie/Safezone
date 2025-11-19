<template>
  <div class="game-card" @click="$emit('click')">
    <div class="card-image">
      {{ emoji }}
    </div>
    <div class="card-content">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
      <div class="card-stats">
        <span>⭐ {{ rating }}</span>
        <span>👥 {{ players }}</span>
      </div>
      <button class="btn-play">Play Now</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  description: String,
  rating: String,
  players: String,
  emoji: {
    type: String,
    default: '🎮'
  }
})

defineEmits(['click'])
</script>

<style scoped>
.game-card {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.game-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(248, 117, 170, 0.2);
}

.card-image {
  height: 200px;
  background: linear-gradient(135deg, var(--primary-light) 0%, var(--accent) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
}

.card-content {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  flex: 1;
}

.card-content h3 {
  font-size: 1.25rem;
  color: var(--dark);
  margin: 0;
}

.card-content p {
  color: #6B7280;
  font-size: 0.875rem;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin: 0;
}

.card-stats {
  display: flex;
  gap: 1rem;
  font-size: 0.875rem;
  color: #9CA3AF;
}

.btn-play {
  background: linear-gradient(135deg, var(--primary) 0%, #FF6B9D 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  margin-top: auto;
}

.btn-play:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(248, 117, 170, 0.4);
}

.btn-play:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .card-image {
    height: 160px;
    font-size: 3rem;
  }

  .card-content {
    padding: 1rem;
  }

  .card-content h3 {
    font-size: 1.1rem;
  }
}
</style>
