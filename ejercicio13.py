#Ejercicio 13: 
# Crear un programa que pida al usuario un número entero y 
# muestre por pantalla
#si es par o impar.

numero = int( input( "Intruduce un num entero:"))

if numero % 2 == 0: # esto quiere decir que es par
        print("El número es par")
else:
        print("El número es impar")