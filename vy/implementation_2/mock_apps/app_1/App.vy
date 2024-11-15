section Template:
    <div id: "hello">
        Hello
    </div>
    <div>
        Count is {{ count }}
    </div>
    # Notice, I can have a Python comment here (or anywhere I want).
    # Notice, I did not wrap the click to increment nor give click an @
    <div
        id: "clickme" 
        click: increment
        style: { background_color: "green", width: "100px" }
    >
        Click me to raise count!
    </div>

section Script:
    count = ref(0)

    def increment():
        count.value += 1