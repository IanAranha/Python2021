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
bubbleSort(arr)
bubbleSort(arr2)
