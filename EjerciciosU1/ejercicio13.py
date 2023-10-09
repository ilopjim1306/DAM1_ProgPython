n = float(input("Introduce un primer número:"))
m = float(input("Introduce un segundo número:"))
c = n // m
r = n % m

print(f"la división de {n} entre {m} da un cociente {c} y un resto {r}")

#manera para poner dos decimales
print("la división de {:.2f} entre {:.2f} da un cociente {:.2f} y un resto {:.2f}".format(n, m, c, r))