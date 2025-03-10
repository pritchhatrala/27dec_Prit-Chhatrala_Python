class Father:
    def work(self):
        print("Father is working")

class Mother:
    def cook(self):
        print("Mother is cooking")

class Child(Father, Mother):
    def play(self):
        print("Child is playing")

child = Child()

child.work()  
child.cook()  
child.play()  