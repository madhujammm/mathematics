def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))    


# WITHOUT RECURSION
def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(Factorial(2))