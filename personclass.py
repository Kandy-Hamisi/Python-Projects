class Person:

    # Constructor method
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name}, You like talking alot")
        


kandy = Person("Kandy Hamisi Said")
kandy.talk()