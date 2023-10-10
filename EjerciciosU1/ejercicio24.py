precio = input("Introduce el precio del producto en euros: ")
precio = precio.split(".")

print(f"El precio del producto es: {precio[0]} euros y {precio[1]} céntimos.")