<template>
  <div class="flex border-b border-gray-300">
    <button
      v-for="tab in tabs"
      :key="tab"
      @click="$emit('update:modelValue', tab)"
      :class="[
        'px-4 py-2',
        tab === modelValue ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-600'
      ]"
    >
      {{ tab }}
    </button>
  </div>
</template>

<script setup lang="ts">
defineProps({
  tabs: { type: Array as () => string[], required: true },
  modelValue: { type: String, required: true }
})
defineEmits(['update:modelValue'])
</script>
