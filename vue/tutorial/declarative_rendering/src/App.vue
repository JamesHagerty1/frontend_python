<script setup>
// TODO figure out how to user vue-router
    // import { RouterLink, RouterView } from 'vue-router'

    import { reactive, ref } from 'vue'

    const counter = reactive({ count: 42 })
    const message = ref('Hello World!')
</script>


<template>
    <!--
    Notice, no need to include .value for objects with reactivity, in the
    template.
    -->
    <h1>{{ message }}</h1>
    <p>Count is: {{ counter.count }}</p>
</template>


<style scoped>

</style>
