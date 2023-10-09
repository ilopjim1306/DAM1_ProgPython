productos = input("Introduce los productos de la cesta de la compra separado por comas: ")
productos = productos.split(",")

print ('\n' .join(map(str, productos)))