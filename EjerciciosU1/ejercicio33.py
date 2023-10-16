# Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.
#
# > Dame 3 números:
# > 14
# > 7
# > 10
# > Tus números son 7 10 14

# Inicio
# 	Escribe "Dame 3 números: "
# 	Lee n1
# 	Lee n2
# 	Lee n3
# 	Si (n1 < n2 and n1 < n3) entonces
# 		Si (n2 < n3) entonces
# 			Escribe n1 + " " + n2 + " " + n3
# 		Sino
# 			Escribe n1 + " " + n3 + " " + n2
# 	Sino
# 		Si (n2 < n1 and n2 < n3) entonces
# 			Si (n1 < n3) entonces
# 				Escribe n2 + " " + n1 + " " + n3
# 			Sino
# 				Escribe n2 + " " + n3 + " " + n1
# 		Sino
# 			Si (n3 < n1 and n3 < n2) entonces
# 				Si (n1 < n2) entonces
# 					Escribe n3 + " " + n1 + " " + n2
# 				Sino
# 					Escribe n3 + " " + n2 + " " + n1
# Fin



# Manera 1 separando los inputs
# n1 = int(input("Dame un número: "))
# n2 = int(input("Dame otro número: "))
# n3 = int(input("Dame otro más número: "))

#Manera 2 con un solo input
n = input("Dame 3 números: ")
n = n.split(" ")
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])

print(n1)
print(n2)
print(n3)

if (n1 < n2 and n1 < n3):
    if (n2 < n3):
        print(f"Tus números son {n1} {n2} {n3}")
    else:
        print(f"Tus números son {n1} {n3} {n2}")
else:
    if (n2 < n1 and n2 < n3):
        if (n1 < n3):
            print(f"Tus números son {n2} {n1} {n3}")
        else:
            print(f"Tus números son {n2} {n3} {n1}")
    else:
        if (n3 < n1 and n3 < n2):
            if (n1 < n2):
                print(f"Tus números son {n3} {n1} {n2}")
            else:
                print(f"Tus números son {n3} {n2} {n1}")