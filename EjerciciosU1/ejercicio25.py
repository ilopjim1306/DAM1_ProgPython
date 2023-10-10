fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
fecha1 = fecha.split("/")
dia= int(fecha1[0])
mes = int(fecha1[1])
anio= int(fecha1[2])

print("Día {:02d} del mes {:02d} del año {}" .format(dia, mes, anio))