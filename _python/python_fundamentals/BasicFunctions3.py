# Biggie Size - Given an array, write a function that changes all positive
# numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that
# same array, changed to [-1, "big", "big", -5].

def biggieSize(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

print(biggieSize([-1,3,5,-5]))



# Count Positives - Given an array of numbers, create a function to replace last
# value with number of positive values. Example, countPositives([-1,1,1,1])
# changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered
# to be a positive number).
#
def countPositives(arr):
    counter=0
    print(arr)
    for i in range(0, len(arr)):
        if arr[i] > 0:
            counter += 1
    arr[len(arr)-1] = counter
    return arr

print(countPositives([-1,1,1,1,0,-1,2,3,0,22]))




# SumTotal - Create a function that takes an array as an argument and returns the
# sum of all the values in the array.  For example sumTotal([1,2,3,4]) should
# return 10
#
def sumTotal(arr):
    sum=0
    for i in range(0, len(arr)):
        sum+=arr[i]
    return sum

print(sumTotal([1,2,3,4]))
print(sumTotal([-1,-2,-3,-4]))


# Average - Create a function that takes an array as an argument and returns the
# average of all the values in the array.  For example multiples([1,2,3,4]) should
# return 2.5

def arrAverage(arr):
    arrTotal = sumTotal(arr)
    avg = arrTotal/len(arr)
    return avg

print(arrAverage([1,2,3,4]))
print(arrAverage([3,6,9,12,15,18,21]))

# Length - Create a function that takes an array as an argument and returns the
# length of the array.  For example length([1,2,3,4]) should return 4
#

def arrLength(arr):
    return len(arr)

print(arrLength([1,2,3,4]))
print(arrLength([]))
print(arrLength([1,2,3,4,5,6,7,8,9]))


# Minimum - Create a function that takes an array as an argument and returns the
# minimum value in the array.  If the passed array is empty, have the function
# return false.  For example minimum([1,2,3,4]) should return 1;
# minimum([-1,-2,-3]) should return -3.

def arrMinimum(arr):
    if len(arr) == 0:
        return False
    else:
        min = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < min:
                min = arr[i]
        return min

print(arrMinimum([1,2,3,4]))
print(arrMinimum([]))
print(arrMinimum([20,44,-3,22,33,55,9,12,3,8]))
print(arrMinimum([20,44,-3,22,33,55,9,-12,3,8]))



# Maximum - Create a function that takes an array as an argument and returns the
# maximum value in the array.  If the passed array is empty, have the function
# return false.  For example maximum([1,2,3,4]) should return 4;
# maximum([-1,-2,-3]) should return -1.
#
def arrMaximum(arr):
    if len(arr) == 0:
        return False
    else:
        max = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
        return max

print(arrMaximum([1,2,3,4]))
print(arrMaximum([]))
print(arrMaximum([20,44,-3,22,33,55,9,12,3,8]))
print(arrMaximum([20,44,-3,22,33,55,9,-12,3,8]))





# UltimateAnalyze - Create a function that takes an array as an argument and
# returns a dictionary that has the sumTotal, average, minimum, maximum and length
# of the array.
def ultimateAnalyze(arr):
    dict = {}
    dict["Total"] = sumTotal(arr)
    dict["Average"] = arrAverage(arr)
    dict["Minimum"] = arrMinimum(arr)
    dict["Maximum"] = arrMaximum(arr)
    dict["Length"] = arrLength(arr)
    return dict


print(ultimateAnalyze([1,3,5]))
print(ultimateAnalyze([20,44,-3,22,33,55,9,-12,3,8]))
#
# ReverseList - Create a function that takes an array as an argument and return
# an array in a reversed order.  Do this without creating an empty temporary
# array.  For example reverse([1,2,3,4]) should return [4,3,2,1].
# This challenge is known to appear during basic technical interviews.

def reverseList(arr):
    forward = 0
    mid = len(arr)/2
    back=len(arr)-1
    while forward < mid:
        temp = arr[forward]
        arr[forward] = arr[back]
        arr[back] = temp
        forward+=1
        back-=1
    return arr

print(reverseList([1,2,3,4]))
print(reverseList([30,40,50,65,75,85,95]))

# Redoing the above with one less variable
def bak(arr):
    counter=0
    mid = int(len(arr)/2)
    while counter < mid:
        temp = arr[counter]
        arr[counter] = arr[len(arr)-1-counter]
        arr[len(arr)-1-counter] = arr[temp]
        counter+=1
    return arr
print(bak([1,2,3,4,5]))
print(reverseList([30,40,50,65,75,85,95]))
