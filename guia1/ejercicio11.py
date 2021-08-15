#Ejercicio 11: 
# Crear un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable

contrasena = "contraseña"
contrasena_us = input("Ingrese su contraseña: ")

if contrasena == contrasena_us:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")