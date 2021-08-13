#Ejercicio 4: Crear un programa que pregunte el nombre del usuario y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.




nombre = input("Ingrese su nombre: ")
print(nombre)


n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

n = int( input( "Intruduce un num entero:"))

print (( nombre * int (n)))

for i in range (n):
    print(nombre)


nombre = input("Ingrese su nombre: ")
n = int(input("Introduce un número entero: "))

print((f"{nombre}\n" * n ))