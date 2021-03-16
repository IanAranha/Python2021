# using SUPER to do Animal class and stuff

class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def mainDisplayHealth(self):
        print(f"\nName:{self.name} \nCurrent Health:{self.health}")
        return self


class Dog(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super().mainDisplayHealth()
        print("I am a dragon")


a = Animal("Simba")
print(a)
a.mainDisplayHealth()
a.walk().walk().walk()
a.mainDisplayHealth()
a.run().run()
a.mainDisplayHealth()


d = Dog("Emma")
print(d)
d.mainDisplayHealth()
d.walk().walk().walk()
d.mainDisplayHealth()
d.run().run()
d.mainDisplayHealth()
d.pet().pet().pet()
d.mainDisplayHealth()

b = Dragon("Gladiator")
b.displayHealth()
