def factorial(n):
    if n < 0:
        return -1
    if n <= 1:
        return 1
    total = 1
    while n > 0:
        total = n * total
        n -= 1
    return total

def factorialstr(n):
    if n < 0:
        return -1
    if n <= 1:
        return 1
    total = 1
    frase = (f"{n}! = ")
    while n > 1:
        total = n * total
        n -= 1
        if n > 1:
            frase = frase + str(n) + " x "
        else:
            frase = frase + str(n)
    return frase + " = " + str(total)



n = int(input("Introduce un número de inicio: "))

print(factorial(n))
print(factorialstr(n))




