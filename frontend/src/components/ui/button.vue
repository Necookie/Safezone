<template>
  <button :class="['btn', `btn-${variant}`, `btn-${size}`]">
    <slot />
  </button>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'accent', 'ghost'].includes(value)
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  }
})
</script>

<style scoped>
.btn {
  font-weight: 600;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  font-family: inherit;
}

/* Primary Button */
.btn-primary {
  background: linear-gradient(135deg, var(--primary) 0%, #FF6B9D 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(248, 117, 170, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(248, 117, 170, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}

/* Secondary Button */
.btn-secondary {
  background: var(--secondary);
  color: var(--dark);
  border: 2px solid var(--secondary);
}

.btn-secondary:hover {
  background: var(--accent);
  border-color: var(--accent);
  transform: translateY(-2px);
}

/* Accent Button */
.btn-accent {
  background: var(--accent);
  color: white;
  box-shadow: 0 4px 12px rgba(174, 222, 252, 0.3);
}

.btn-accent:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(174, 222, 252, 0.4);
}

/* Ghost Button */
.btn-ghost {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-ghost:hover {
  background: var(--primary-light);
  transform: translateY(-2px);
}

/* Sizes */
.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.btn-md {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

.btn-lg {
  padding: 1rem 2rem;
  font-size: 1.125rem;
}

@media (max-width: 640px) {
  .btn {
    width: 100%;
  }
}
</style>
