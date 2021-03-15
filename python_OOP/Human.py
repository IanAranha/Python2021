# Learning about super


class Human:
    def __init__(self):
        self.health = 5
        self.intelligence = 3
        self.strength = 2
        self.stealth = 2

class Wizard(Human):
    def __init__(self):
        super().__init__() ###Super calls the Human __init__ down here and gives each class same attributes
        self.intelligence = 10

    def heal(self):
        self.health += 10  ##Only wizards can heal their health.


class Ninja(Human):
    def __init__(self):
        super().__init__() ###Super calls the Human __init__ down here and gives each class same attributes
        self.stealth = 10

    def steal(self):
        self.stealth += 5


class Samurai(Human):
    def __init__(self):
        super().__init__() ###Super calls the Human __init__ down here and gives each class same attributes
        self.strength = 10

    def sacrifice(self):
        self.health -= 5



h = Human()
print(h)
print(f"Health: {h.health} \nIntelligence: {h.intelligence} \nStrength: {h.strength} \nStealth: {h.stealth}")

w = Wizard()
print(w)
print("Created a new Wizard")
print(f"Health: {w.health} \nIntelligence: {w.intelligence} \nStrength: {w.strength} \nStealth: {w.stealth}")

n = Ninja()
print(n)
print("Created a new Ninja")
print(f"Health: {n.health} \nIntelligence: {n.intelligence} \nStrength: {n.strength} \nStealth: {n.stealth}")

s = Samurai()
print(s)
print("Created a new Samurai")
print(f"Health: {s.health} \nIntelligence: {s.intelligence} \nStrength: {s.strength} \nStealth: {s.stealth}")
