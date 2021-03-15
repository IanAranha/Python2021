# Inheritance. The main class has attributes and methods that apply to all the
# children classes. The children class can have their own properties and Methods
# that are unique to them only.

class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        return self

    def reverse(self, miles):
        self.mileage -= miles
        return self


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self

class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self


v = Vehicle(4, 8, "dodge", "minivan")
print("\n")
print("Object:", v)
print("Wheels:",v.wheels)
print("Capacity:",v.capacity)
print("Make:",v.make)
print("Model:",v.model)
print("Mileage",v.mileage)

b = Bike(2,1, "schwinn", "paramount")
print("\n")
print("Object:", b)
print("Type:",b.vehicle_type())
print("Wheels:",b.wheels)
print("Capacity:",b.capacity)
print("Make:",b.make)
print("Model:",b.model)
print("Mileage",b.mileage)

c = Car(8, 5, "Toyota", "Matrix")

print("\n")
print("Object:", c)
print("Wheels:",c.wheels)
print("Capacity:",c.capacity)
print("Make:",c.make)
print("Model:",c.model)
print("Mileage",c.mileage)
print("Running 'SET_WHEELS'")
c.set_wheels()
print("Wheels:",c.wheels)

a = Airplane(22,853,"Airbus","A380")
print("\n")
print("Object:", a)
print("Wheels:",a.wheels)
print("Capacity:",a.capacity)
print("Make:",a.make)
print("Model:",a.model)
print("Mileage",a.mileage)
print("Running 'FLY'")
a.fly(3000)
print("Mileage",a.mileage)
