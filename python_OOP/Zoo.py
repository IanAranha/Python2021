import Animal

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []


    def addDog(self, name):
        self.animals.append(Animal.Dog(name))

    def addDragon(self, name):
        self.animals.append(Animal.Dragon(name))

    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.mainDisplayHealth()

zoo1 = Zoo("Ian's Zoo")
zoo1.addDog("Cosette")
zoo1.printAllHealth()
