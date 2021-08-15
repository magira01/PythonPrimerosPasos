#Ejercicio 18: 
# Crear un programa que pida al usuario una palabra y luego muestre por
#pantalla una a una las letras de la palabra introducida empezando por la última

palabra = input("Ingrese una palabra: ")
for letra in palabra[::-1]:
    print(letra)

palabra = input("Ingrese una palabra: ") # esta es otra manera de realizarlo
for letra in reversed(palabra):
    print(letra)   