class Animal(object):

    def __init__(self):
        print("Animail Created")

    def whoAmI(self):
        print ("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("woof")

a = Dog()

a.eat()
a.whoAmI()