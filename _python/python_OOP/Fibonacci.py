def fib(n):
    result_array=[]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-2) + fib(n-1)
        return result
print(fib(7))


