<template>
    <div id="hello">
        Hello!
    </div>
    <div>
        Count: {{ count }}
    </div>
    <div 
        id="clickme" 
        @click="increment"
    >
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

<vython>
    import ref from vython

    count = ref(0)

    def increment()
        count.value += 1
</vython>