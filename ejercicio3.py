#Ejercicio 3: Crear un programa que pida al usuario nombre y edad e imprima dichos
#datos en renglones distintos.

nombre = input("Ingrese su nombre: ")
print(nombre)

edad = input ("Ingrese su edad: ")
print(edad)

print()
print(nombre); print(edad) # el ; nos habla de que estamos hablando de dos senencias disintas y las va a escribir en dos renglones disntintos.

print()
print(f"{nombre} \n {edad}") # f cadena de texto y con \n se genera el espacio