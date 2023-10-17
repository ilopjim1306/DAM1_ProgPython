#Ejercicio 4 con funciones
#1.4 => NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.

def temperatura():
    far = float(input("Ingresa la temperatura en Farenheit: "))
    return round((far - 32) * 5/9,2)

print("La temperatura en Celsius es: ", temperatura())