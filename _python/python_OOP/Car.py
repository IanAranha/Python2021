# Create a class called  Car. In the __init__(), allow the user to specify the
# following attributes: price, speed, fuel, mileage. If the price is greater than
# 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car. In the class have a method
# called display_all() that returns all the information about the car as a string.
# In your __init__(), call this display_all() method to display information
# about the car once the attributes have been defined.

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print(f"\n\nPrice: {self.price} \nSpeed:{self.speed}mph \nFuel: {self.fuel} \nMileage: {self.mileage} \nTax:{self.tax}")
        return self


car1=Car(29344, 180, "Full", 250)
car2=Car(8399, 130, "Half", 87332)
car3=Car(13332, 250, "Empty", 300)
car4=Car(17499, 200, "Quarter", 54229)
car5=Car(22200, 170, "Half", 13999)
car6=Car(9300, 180, "Full", 22033)
