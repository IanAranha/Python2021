# Creating Bike class as part of Coding Dojo assignments

# Create a new class called Bike with the following properties/attributes:
#         price
#         max_speed
#         miles
#
# Create 3 instances of the Bike class.
#
# Use the __init__() method to specify the price and max_speed of each instance
# (e.g. bike1 = Bike(200, "25mph"); In the __init__(), also write the code so
# that the initial miles is set to be 0 whenever a new instance is created.
#
# Add the following methods to this class:
#
# displayInfo() - have this method display the bike's price, maximum speed, and
# the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles
# ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total
# miles ridden by 5.


class Bike:

    # Attributes
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0


    # Methods
    def displayNewInfo(self):
        print(f"Price: {self.price}, \nMaximum Speed: {self.max_speed}, \nMiles: {self.miles}")
        return self

    def displayInfo(self):
        print(f"Miles: {self.miles}")
        return self

    def ride(self):
        print("Riding...")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing...")
        if self.miles > 5:
            self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(190, "20mph")
bike3 = Bike(230, "30mph")
bike1.displayNewInfo()
bike2.displayNewInfo()
bike3.displayNewInfo()

# Have the first instance ride three times, reverse once and have it
# displayInfo().
print("Bike 1 at start:")
bike1.displayInfo().ride().ride().ride().reverse()
print("Bike 1 after methods")
bike1.displayInfo()

# Have the second instance ride twice, reverse twice and have it displayInfo().
print("Bike 2 at start:")
bike2.displayInfo().ride().ride().reverse().reverse()
print("Bike 2 after methods")
bike2.displayInfo()


# Have the third instance reverse three times and displayInfo().
print("Bike 3 at start:")
bike3.displayInfo().reverse().reverse().reverse()
print("Bike 3 after methods")
#Testing that reversing does not cause MILES to go
# beyond 0.
bike3.displayInfo()

#Testing that reversing works still
bike3.displayInfo().ride().ride().ride().reverse()
bike3.displayInfo()
