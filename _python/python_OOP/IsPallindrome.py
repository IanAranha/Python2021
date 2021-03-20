def isPallindrome(str):
    mid = int(len(str)/2)
    for i in range(0, mid):
        if str[i] == str[len(str)-1-i]:
            continue
        else:
            return False
    return True 



print(isPallindrome("supercalifragilistic"))
print(isPallindrome("racecar"))