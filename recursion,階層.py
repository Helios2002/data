def factorial(n):
    if n == 0:
        return 1
    if n > 0:
        s = n*factorial(n-1)
        return s
print(factorial(3))


            
            
            