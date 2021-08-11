#Ejercicio 17: 
# Crear un programa que muestre por pantalla la tabla de multiplicar 
# del 1 al 10.

for numero in range( 1, 11):
    print(f"Tabla de multiplicar del {numero}")
    for digito in range (10):
        print(f"{numero}x{digito} = {numero * digito}")

        print()