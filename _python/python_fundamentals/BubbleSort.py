arr = [4,2,5,1,0,8]
arr2 = [33,87, 9, 54, 11, 40,76, 26, 69, 88, 17, 1]
def bubbleSort(arr):
    print("Start array:", arr)
    for j in range(0,len(arr)-1):
        print("\n\n","-"*40,"\bITERATION ", j+1, "-"*40)
        for i in range(len(arr)-1-j):
            print("\n","*"*80)
            print("Index: ", i, "Value:", arr[i], "Next Value", arr[i+1])
            print("Comparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print("Swapped", arr[i+1], arr[i])
            else:
                print("No need to swap")
            print("Array is now: ", arr)
            print("*" * 70)

#
# bubbleSort(arr)
# bubbleSort(arr2)


arr3 = [6,4,5,3,2,1]

def bubbleSort2(arr):
    print("Starting array", arr)
    for i in range(0, len(arr)-1):
        print("x" * 40, "Iteration", i+1, "x" * 40)
        for j in range(0, len(arr)-1-i):
            print("Comparing", arr[j], arr[j+1])
            if arr[j] > arr [j+1]:
                print("Swapping", arr[j], arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                print("No Swap needed")
            print("Array is now: ",arr)


bubbleSort2(arr3)
