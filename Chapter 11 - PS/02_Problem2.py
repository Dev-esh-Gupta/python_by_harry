class Animals:
    category = "mammels"

class Pets(Animals):
    type = "Domestic"

class Dog(Pets):
    def bark(self):
        print(f"Dog is Barking, is of type {self.type} and comes under category {self.category}")

broomo = Dog()

broomo.bark()

