#Ejercicio 5 con funciones
#1.5 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def conIVA(SinIVA, IVA):
    print("El total con IVA es:", round(SinIVA * (IVA/100+1),2) , "€")

SinIVA = float(input("Importe sin IVA: "))
IVA = float(input("Tipo de IVA: "))

conIVA(SinIVA, IVA)