#Desarrolla una función en prueba1.py que reciba dos números y retorne el mayor número de los dos o 0 si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest desde la terminal (puedes hacerlo en la terminal dentro de Visual Studio Code).

def mayor(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 0
    else:
        return num2
    
num1 = 6
num2 = 3

print(mayor(num1, num2))