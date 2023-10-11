#Inicio
#   Escribe "Dame un número de inicio: "
#   Lee inicio
#   Escribe "Dame un número de incremento: "
#   Lee incremento
#   Escribe "Dame un número final: "
#   Lee total
#   serie = "SERIE => " + inicio
#   cont = inicio
#   Si (incremento < 0) entonces
#       Mientras (incremento < 0)
#           Escribe "Error introduce un incremento mayor a 0: "
#           Lee incremento
#   Si (total < 0) entonces
#       Mientras(total < 0)
#           Escribe "Error introduce un total mayor a 0: "
#           Lee total
#   mientras (cont < total) hacer
#       inicio = inicio + incremento       
#       cont = cont + 1
#       Si (cont < (total - 1)) entonces
#           serie = serie + inicio + ".."
#       Sino 
#           Si (cont == total) entonces
#               serie = serie + inicio
#           Sino 
#               serie = serie + inicio + "-"
#Fin

inicio = int(input("Dame un número de inicio: "))
incremento = int(input("Dame un número de incremento: "))
total = int(input("Dame un número final: "))
serie = "SERIE => " + str(inicio) +  "-"
cont = 1

while(incremento <= 0 or total <= 0):
    incremento = int(input("Error introduce un incremento mayor a 0: "))
    total = int(input("Error introduce un final mayor a 0: "))
while (cont < total):
    inicio = inicio + incremento
    cont = cont + 1
    if (cont < (total - 1)):
        serie = serie + str(inicio) + ".."
    else:
        if (cont == total):
            serie = serie + str(inicio)
        else:
            serie = serie + str(inicio) + "-"

print(serie)
