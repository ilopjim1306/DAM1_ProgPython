#Inicio
#   Lee nombre
#   Lee edad
#   Si (nombre == "") entonces
#       nombre = "Desconocido"
#   Si (edad < 0 or edad >125)
#       while (edad < 0 or edad >125) entonces
#           Lee edad
#   Si (edad > 0 or edad < 125) entonces
#       restante = 125 - edad
#       Escribe "Te llamas " + nombre + " y tienes " + edad + ", te quedan aún " + restante + " años por cumplir."
#
#Fin

nombre = input("Escribe tu nombre: ")
edad = int(input("Dame tu edad: "))

if (nombre == ""):
    nombre = "Desconocido"
if (edad < 0 or edad > 125):
    while (edad < 0 or edad > 125):
        edad = int(input("Escribe de nuevo tu edad: "))
if (edad > 0 or edad < 125):
    restante = 125 - edad
    print(f"Te llamas {nombre} y tienes {edad}, te quedan aún {restante} años por cumplir.")