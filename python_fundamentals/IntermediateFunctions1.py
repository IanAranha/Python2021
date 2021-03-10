def beCheerful(name="", repeat=""):
    if repeat:
        print(f"Hello {name} " * int(repeat))
    else:
        print(f"Hello {name}")

beCheerful()
beCheerful("Ian")
beCheerful(name="Andrew", repeat=5)


import random
print(random.random()) #Prints random float between 0.0 and 0.99
print(random.random() * 50) ## Prints random number between 0 and 50
print(int(3.1433))
print(round(3.655))

# As part of this assignment, please create a function randInt() where

# randInt() returns a random integer between 0 to 100
# def randInt():
#     randInt = (random.random() * 100)
#     return randInt
#
# for i in range(1, 31):
#     print(i," - ",round(randInt(),2))
#
# # randInt(max=50) returns a random integer between 0 to 50
# def randIntMax(max=50):
#     randInt = (random.random() * max)
#     return randInt
#
# for i in range(1, 31):
#     print(i," - ",round(randIntMax(),2))
#
# # randInt(min=50) returns a random integer between 50 to 100
# def randIntMinMax(min=50, max=100):
#     randInt = (random.random() * (max - min) + min)
#     return randInt
#
# for i in range(1, 31):
#     print(i," - ",round(randIntMinMax(),1))
#
#
# # randInt(min=50, max=500) returns a random integer between 50 and 500
# def randIntMinMax2(min=50, max=500):
#     randInt = (random.random() * (max - min) + min)
#     return randInt
#
# for i in range(1, 31):
#     print(i," - ",round(randIntMinMax2(),1))

# Create this function without using random.randInt() but you are allowed to use random.random()



#Putting all the above funtions into one

def randInt(min=0, max=100):
    randInt = random.random() * (max - min) + min
    return round(randInt,2)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=100))
print(randInt(min=50, max=500))
