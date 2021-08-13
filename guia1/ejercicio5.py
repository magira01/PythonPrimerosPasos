#Ejercicio 5: Crear un programa que pregunte el nombre del usuario y después de que
#el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras.


nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

nombre = input("¿Cómo te llamas? ")
cont = 0 #metodo cont , sirve ara contar en este caso las letras que tiene una varible
for letra in nombre:
    cont +=1
print(f"{nombre} tiene {cont} letras")

nombre = input("¿Cómo te llamas? ")
cont= len(nombre) #decelce la cantidadde elementos del objeto iterable qye en este caso es el nombre
print(f"{nombre} tiene {cont} letras")
