nums1 = [5,9,3,20,4,11,2]
nums2 = [22,54,9,18,77,91,83,86,77,15,93,35]

def selectionSort(nums):
    print("Start array before any sorting:", nums)
    for i in range(0, len(nums)):
        print("\n", "-"*50, "\bITERATION", i+1, "-"*50)
        print("Array to be sorted", nums)
        min_index = i
        print("Pointer is at: ", nums[i])
        print("Comparing all numbers to right of ", nums[i], "looking for the minimum value.")

        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                print(nums[j], "is lower than", nums[min_index])
                min_index = j
                print("New Min index:", min_index, " New min value:", nums[min_index])
            else:
                print(nums[j], "is not lower than", nums[min_index])
        print("Swapping", nums[i], nums[min_index])
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print("Array is now:", nums)

selectionSort(nums1)
# selectionSort(nums2)
