# Countdown - Create a function that accepts a number as an input.  Return a new
# list that counts down by one, from the number (as lists 'zero'th element) down
# to 0 (as the last element).  For example countDown(5) should return
# [5,4,3,2,1,0].

def countdown(num):
    list = []
    while num >= 0:
        list.append(num)
        num -= 1
    return list

print(countdown(5))
print(countdown(100))


# Print and Return - Your function will receive a list with two numbers. Print
# the first value, and return the second.

def printAndReturn(list):
    print(list[0])
    return list[1]

printAndReturn([1,10])
print(printAndReturn([5, 10]))


# First Plus Length - Given a list, return the sum of the first value in the list,
# plus the list's length.

def firstPlusLength(list):
    sum = 0
    if len(list) == 0:
        return 0
    else:
        sum = list[0] + len(list)
    return sum

print(firstPlusLength([1,2,3,4,5]))
print(firstPlusLength([]))
print(firstPlusLength([5,10,15,20,25]))


# Values Greater than Second - Write a function that accepts a list, and returns
# a new list with the list values that are greater than its 2nd value.  Print
# how many values this is.  If the list is only one element long, have the function
# return False

def valuesGreaterThanSecond(list):
    if len(list) < 2:
        return False
    else:
        new_list = []
        for i in range(0, len(list)):
            print(list[i])
            if list[i] > list[1]:
                new_list.append(list[i])
        print(len(new_list))
        return new_list

valuesGreaterThanSecond([1,2,3,4,5])
valuesGreaterThanSecond([1,3,5,7])
valuesGreaterThanSecond([0])

# This Length, That Value - Write a function called lengthAndValue which accepts
# two parameters, size, and value. This function should take two numbers and
# return a list of length size containing only the number in value. For example,
# lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(a, b):
    new_list=[]
    while len(new_list) != a:
        new_list.append(b)
    return new_list

print(lengthAndValue(4,7))
