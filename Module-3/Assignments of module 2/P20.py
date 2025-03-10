global_var = "I am a global variable"

class Demo:
    def __init__(self, value):
        self.instance_var = value 

    def show_variables(self):
        local_var = "I am a local variable"  
        print(f"Global Variable: {global_var}")
        print(f"Instance Variable: {self.instance_var}")
        print(f"Local Variable: {local_var}")

obj = Demo("I am an instance variable")

obj.show_variables()
