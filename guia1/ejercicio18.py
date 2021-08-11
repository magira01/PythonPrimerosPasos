#Ejercicio 18: 
# Crear un programa que pida al usuario una palabra y luego muestre por
#pantalla una a una las letras de la palabra introducida empezando por la última

frase = input("Ingrese una frase: ")
letra= input("Ingrese una letra: ")

cont = 0
for caracter in frase:
    if caracter == letra:
        cont += 1