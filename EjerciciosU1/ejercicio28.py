#Inicio
#   Escribe "Dame un número"
#   Lee n1
#   Escribe "Dame otro número"
#   Lee n2
#   n3 = 0
#   Si (n1 == n2) entonces
#       Escribe "Los números no pueden ser iguales"
#   Sino si (n1 < n2)
#        n3 = n2 - n1
#       Escribe "El menor de los dos es " + n1 + "y entre ellos existen " + n3 + "números enteros"
#    Sino si (n1 > n2)
#       n3 = n1 -n2
#       Escribe "El menor de los dos es " + n2 + "y entre ellos existen " + n3 + "números enteros"
#Fin

n1  = int(input("Dame un número: "))
n2 = int(input("Dame otro número: "))
n3 = 0
if (n1 == n2):
    print("Los números no pueden ser iguales")
elif (n1 < n2):
    n3 = n2 - n1
    print(f"El número menor es el {n1} y entre ellos exiten {n3} números enteros")
elif (n1 > n2):
    n3 = n1 - n2
    print(f"El número menor es el {n2} y entre ellos exiten {n3} números enteros")
