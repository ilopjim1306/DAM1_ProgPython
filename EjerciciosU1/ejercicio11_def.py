#Ejercicio 11 con funciones
#1.11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.

def suma(n):
    return f"Suma = {n} * ({n} + 1)/2 = {n * (n + 1)/2}"

n= int(input("Introduce un número positivo: "))

print(suma(n))

