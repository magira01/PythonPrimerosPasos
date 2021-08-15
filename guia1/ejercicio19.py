#jercicio 19: 
# Crear un programa en el que se pregunte al usuario por una frase 
# y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = 0 # utilizamos el contador

for caracter in frase:
    if caracter == letra:
        cont += 1

print(f"La frase contiene la letra {letra} {cont} veces")


frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
cont = frase.count(letra) # utilizando el metodo count

print(f"La frase contiene la letra {letra} {cont} veces")

