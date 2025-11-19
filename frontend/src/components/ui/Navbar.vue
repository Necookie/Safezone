<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="navbar-brand">
        🎮 Safezone
      </router-link>
      
      <div class="navbar-menu">
        <router-link to="/" class="nav-link">
          Home
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script setup>
</script>

<style scoped>
.navbar {
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  padding: 1rem 2rem;
  box-shadow: 0 4px 12px rgba(248, 117, 170, 0.15);
  position: sticky;
  top: 0;
  z-index: 50;
}

.navbar-container {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.navbar-brand:hover {
  transform: scale(1.05);
}

.navbar-menu {
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 500;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: white;
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
  }

  .navbar-brand {
    font-size: 1.25rem;
  }

  .navbar-menu {
    gap: 1rem;
  }
}
</style>
