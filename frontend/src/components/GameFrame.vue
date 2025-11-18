<template>
  <iframe 
    :src="gameUrl" 
    width="800" 
    height="600" 
    frameborder="0">
  </iframe>
</template>

<script>
export default {
  data() {
    return {
      gameUrl: "http://127.0.0.1:5000/static/games/hill-racing-43/index.html"
    }
  }
}
</script>
