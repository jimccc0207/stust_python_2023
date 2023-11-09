def factorial_loop(n):
    factor = 0
    for i in range(1,n+1):
        factor += i
    return factor

print(factorial_loop(4))