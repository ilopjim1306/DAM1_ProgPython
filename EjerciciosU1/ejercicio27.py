producto = input("Introduce el nombre del producto, su precio y el número de unidades separado por (,): ")
producto = producto.split(",")
nombre = producto[0]
precio = float(producto[1])
cantidad = int(producto[2])
total = precio * cantidad

print("El nombre del producto es: {}, su precio es de: {:6.2f}€, se han vendido un total de {:3d} unidades y el coste total es de: {:8.2f}€.".format(nombre, precio, cantidad, total))