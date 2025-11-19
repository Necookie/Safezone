<template>
  <button
    :class="clsx(
      'px-4 py-2 rounded font-semibold transition',
      variant === 'outline' && 'border border-gray-300',
      variant === 'primary' && 'bg-blue-500 text-white hover:bg-blue-600',
      size === 'icon' && 'p-2'
    )"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
import clsx from 'clsx'

defineProps({
  variant: { type: String, default: 'primary' },
  size: { type: String, default: 'default' }
})
</script>
