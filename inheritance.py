#to reduce repetition

class Mammal:

    def __init__(self, name):
        self.name = name


    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name}, barks")


class Cat(Mammal):
    def best(self):
        print(f"{self.name}, is the best pets")
        


dog1 = Dog("dodge")
dog1.bark()

cat1 = Cat("Lurban")
cat1.best()

# Am happy I now understand inheritance