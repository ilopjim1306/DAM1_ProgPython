capital = float(input("Introduce el dinero depositado: "))
interes = 4/100
primer = capital + (1 + interes)
segundo = primer + (1 + interes)
tercero = segundo + (1 + interes)

print(f"La cantidad de ahorros tras el primer año es de: {round(primer, 2)}€")
print(f"La cantidad de ahorros tras el segundo año es de: {round(segundo, 2)}€")
print(f"La cantidad de ahorros tras el tercer año es de: {round(tercero, 2)}€")