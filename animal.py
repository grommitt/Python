class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print("--------------------------------------")
        print("Name: " + str(self.name))
        print("Health Level: " + str(self.health))
        print("--------------------------------------")

animal = Animal("Monkey", 100)
animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
dog = Dog("Pup")
dog.walk().walk().walk().run().run().pet().pet().display_health()
    
    