producto = input("Introduce el nombre del producto, su precio y el número de unidades separado por (,): ")
producto = producto.split(",")
nombre = producto[0]
precio = float(producto[1])
cantidad = float(producto[2])
total = precio * cantidad

print(f"{nombre.title()}, su precio es de {round(precio,2)}€, con una cantidad de {round(cantidad,2)} unidades y el coste total es de: {round(total, 2)}€")