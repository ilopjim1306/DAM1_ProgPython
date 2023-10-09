SinIVA = float(input("Importe sin IVA: "))
IVA = float(input("Tipo de IVA: "))
conIVA = SinIVA * (IVA / 100 + 1)

print(f"El total con IVA es: {round(conIVA,2)}€")