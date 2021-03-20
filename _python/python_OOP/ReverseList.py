def reverseList(list):
    mid = int(len(list)/2)
    for i in range(0, mid):
        print("Swapping", list[i], list[len(list)-1-i])
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list


