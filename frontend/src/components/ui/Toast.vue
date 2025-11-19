<template>
  <div
    v-if="show"
    class="fixed bottom-4 right-4 bg-gray-800 text-white px-4 py-2 rounded shadow-lg"
  >
    {{ message }}
  </div>
</template>

<script setup lang="ts">
defineProps({
  show: { type: Boolean, default: false },
  message: { type: String, required: true }
})
</script>
