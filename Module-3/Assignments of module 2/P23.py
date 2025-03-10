class Animal:
    def breathe(self):
        print("Animals breathe")

class Mammal(Animal):
    def walk(self):
        print("Mammals can walk")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()

dog.breathe() 
dog.walk()     
dog.bark()    