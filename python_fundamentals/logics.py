#IF statements
age = 19


if age >= 18:
    print("Your age is above 18")
elif age == 17:
    print("You are 17")
else:
    print("you are so young!")



#For Loops

for count in range(0, 5):
    print(count)


ninjas = ['Rozen', 'KB', 'Oliver']
for ninja in ninjas:
    print(ninja)


def sum(a,b):
    print("a:", a, "b:", b) # prints the values of a and b
    return a+b # returns the sum of a+b

print(sum(3,5))
print(sum(2,4)+sum(1,5))


def say_hello(name=""):
    #these lines are indented and therefore part of the function
    if name:
        print('Hello, ' + name + ', from inside the function')
    else:
        print('No name')
# now we're unindented and have ended the previous block
print('Outside of the function')


say_hello()
say_hello("Jo")



#while Loops:

count = 0
while count <= 5:
    print("Looping -", count)
    count +=1



#loop Control
for val in "string":
    if val == "i":
        break
    print(val)


for val in "supercalifragilistic":
    if val == "a":
        continue
    elif val == "c":
        continue
    print(val)



#Else statement:
x = 3
y = x

while y > 0:
    print(y)
    y = y - 1
else:
    print("End of loop")
