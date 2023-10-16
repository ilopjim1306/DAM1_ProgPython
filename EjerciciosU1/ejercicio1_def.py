#Ejercicio 1 con funciones
#1.1 => recibe un nombre y retorna una cadena de caracteres con el resultado.

def nombre():
    n = input("Escribe tu nombre: ")
    return "Hola, " + n + "."

print(nombre())