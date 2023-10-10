#Inicio
#   Lee inicio
#   Lee incremento
#   Lee total
#   Mientras (incremento < 0 and total < 0)
#       Escribe "Error introduce un incremento mayor a 0: "
#       Lee incremento
#   Sino entonces
#       Mientras(total => 0)
#           Escribe "Error introduce un total mayor a 0: "
#           Lee total
#   Para i en (inicio...total) hacer
#       suma = inicio + incremento 
#       Escribe suma       
#
#Fin

inicio = int(input("Dame un número de inicio: "))
incremento = int(input("Dame un número de incremento: "))
total = int(input("Dame un número final: "))

if(incremento <= 0):
    while(incremento <= 0):
        incremento = int(input("Error introduce un incremento mayor a 0: "))
if(total <= 0):
    while(total <= 0):
        total = int(input("Error introduce un final mayor a 0: "))
while (inicio < total):
    inicio = inicio + incremento
    print(inicio)

