class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class overriding the parent method
class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()  
dog.speak()     
