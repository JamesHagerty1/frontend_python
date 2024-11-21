



class App:

    def __template__():
        return """
        <div>
            <div>
                Hello world!
            </div>
            <button onclick="this.hello">
                Click me!
            </button>
        </div>
        """
    
    def hello():
        print("Hello world!")