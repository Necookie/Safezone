<template>
  <Card class="cursor-pointer hover:shadow-lg transition" @click="$emit('click')">
    <img :src="thumbnail" alt="Game thumbnail" class="w-full h-40 object-cover rounded" />
    <h3 class="mt-2 font-bold text-lg">{{ title }}</h3>
    <p class="text-sm text-gray-500">{{ description }}</p>
  </Card>
</template>

<script setup>
import Card from './Card.vue'
defineProps({
  title: String,
  description: String,
  thumbnail: String,
})
defineEmits(['click'])
</script>
