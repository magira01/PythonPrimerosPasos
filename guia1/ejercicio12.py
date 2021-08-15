#Ejercicio 12: 
# Crear un programa que pida al usuario dos números y muestre por
#pantalla su división. Si el divisor es cero, 
# el programa debe devolver un mensaje
#indicando que no se puede dividir por 0.

n1 = int(input("Ingrese un numero entero: "))

n2 = int(input("Ingrese un segundo numero entero: "))


if n2 != 0:
    division = n1 /n2
    print(f"La división entre {n1} y {n2} da como rdo {division}")
else:
    print("No se puede dividir por 0")

# otra manera de hacerlo es, siempre dependiendo de como queramos tratar al 0


numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese otro número: "))

if numero_2 == 0:
    print("No se puede dividir por 0")
else:
    division = numero_1 / numero_2
    print(f"La división entre {numero_1} y {numero_2} da como rdo {division}")
    