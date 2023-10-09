fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
fecha1 = fecha.split("/")

if len(fecha1[0]) == 1:
    fecha1[0] = "0" + fecha1[0]
if len(fecha1[1]) == 1:
    fecha1[1] = "0" + fecha1[1]

print(f"Día {fecha1[0]} del mes {fecha1[1]} del año {fecha1[2]}")