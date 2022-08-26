from abstract_animal import Animal


class Dog(Animal):               # Inherit from abstract base class Animal
    def speak(self):             # speak() *must* be implemented
        print("woof! woof!")


class Cat(Animal):               # Inherit from abstract base class Animal
    def speak(self):             # speak() *must* be implemented
        print("Meow meow meow")


class Duck(Animal):              # Inherit from abstract base class Animal
    pass                         # does NOT implement speak()


d = Dog()
d.speak()

c = Cat()
c.speak()

try:
    d = Duck()  # raises TypeError as it does not meet requirements of Animal
    d.speak()
except TypeError as err:
    print(err)
