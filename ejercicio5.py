#Ejercicio 5: Crear un programa que pregunte el nombre del usuario y después de que
#el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras.


nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")