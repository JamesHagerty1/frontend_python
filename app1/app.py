


class AppRoot:

    def __template__(self):
        return f"""
        <div>
            <div>
                Hello world!
            </div>
            <button @click="self.hello">
                Click me!
            </button>
        </div>
        """
    
    def hello(self):
        print("Hello world!")