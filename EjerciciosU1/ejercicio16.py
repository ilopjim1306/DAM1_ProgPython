pan= 3.49
barranodia= 3.49 * 0.6
vendidanodia= int(input("Barras de pan vendidas: "))
barravendida= barranodia * vendidanodia
print(f"Una barra de pan cuesta {pan}€, pero se descuenta un 60% al no ser fresco.")
print(f"El coste final de todas las barras no frescas es: {round(barravendida, 2)}€.")