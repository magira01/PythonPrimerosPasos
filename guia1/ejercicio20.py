#Ejercicio 20: 
# Crear un programa que muestre el eco de todo lo que el usuario
#introduzca hasta que el usuario escriba “salir” que terminará.

rta = input("Ingrese una palabra :")

while rta != "salir":
    print(rta)

    rta=input("Ingrese una palabra o \nescriba salir para finalizar : ")

 
 # otra manera de hacerlo es con un bucle infinito while true, hasta romperlo creando una condicion.
while True:
    rta = input("Ingrese una palabra o escriba 'salir' para finalizar : ")
    if rta == "salir":
        break
    print(rta)    