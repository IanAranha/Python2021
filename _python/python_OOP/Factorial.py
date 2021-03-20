def factorial(n):
    if n == 1:
        print("Intermediate result for ", n, " * " ,n, "!: ", n)  
        return n
    else:
        result = n * factorial(n - 1)
        print("Intermediate result for ", n, " * " ,n-1, "!: ", result)  
        return result


print(factorial(5))
