numbers = [7,3,11,6,2,1,9]


def insertionSort(arr):
    print("Array to be sorted:", arr)
    # The outer loop. Since the first item at index 0 is already sorted, start at
    # index 1 and move left till end of list.

    for outer_index in range(1, len(arr)):

        # current value is put in a temp location.
        current_value = arr[outer_index]
        print("*" * 30, "Iteration", outer_index,"*" * 30 )
        print("Current value:", current_value)

        # create an inner loop that moves to the right.
        inner_index = outer_index

        #from the current index...move left and move the value to the right if
        # it is larger than the current value
        while inner_index > 0 and arr[inner_index-1] > current_value:
            arr[inner_index] = arr[inner_index-1]
            inner_index -= 1
        arr[inner_index] = current_value
    print("New array", arr)


insertionSort(numbers)
