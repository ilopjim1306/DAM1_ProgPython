#Ejercicio 2 con funciones
#1.2 => recibe horas y coste y retorna el importe total.

def importe(hora, coste):
    return hora * coste

hora= int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))
print("Importe total:", importe(hora, coste), "euros")