<template>
  <div
    class="fixed inset-0 flex items-center justify-center bg-black/50"
    v-if="show"
  >
    <div class="bg-white p-6 rounded-lg max-w-md w-full">
      <slot />
      <button @click="$emit('close')" class="mt-4 px-4 py-2 bg-red-500 text-white rounded">
        Close
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({ show: Boolean })
defineEmits(['close'])
</script>
