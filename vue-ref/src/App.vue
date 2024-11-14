<!--
A minimal Vue app using Vue Single File Components.
-->

<template>
  <div id="hello">
    Hello!
  </div>
  <div>
    Count: {{ count }}
  </div>
  <div id="clickme" @click="increment">
    Click me to raise count!
  </div>
</template>

<style scoped>
  #hello {
    background-color: green;
    width: 120px;
    font-size: 24px;
  }

  #clickme {
    background-color: gray;
    width: 100px;
    font-size: 20px;
  }
</style>

<script setup>
  import { ref } from 'vue'

  const count = ref(0)

  function increment() {
    count.value++
  }
</script>