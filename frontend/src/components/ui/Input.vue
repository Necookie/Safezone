<template>
  <input
    :type="type"
    :placeholder="placeholder"
    class="border rounded px-3 py-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none"
  />
</template>

<script setup lang="ts">
defineProps({
  type: { type: String, default: 'text' },
  placeholder: { type: String, default: '' }
})
</script>
