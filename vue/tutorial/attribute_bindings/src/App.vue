<script setup>
    // TODO figure out how to user vue-router
    // import { RouterLink, RouterView } from 'vue-router'

    import { ref } from 'vue'

    const title_class = ref('title')
</script>


<template>
    <h1 :class="title_class">Make me red</h1>
</template>


<style scoped>
    .title {
        color: red;
    }
</style>
