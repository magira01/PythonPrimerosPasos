#Ejercicio 22: 
# Crear un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y 
# muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debemostrar un mensaje informando de ello.
#Fruta
Banana: 80
Manzana:100
Pera: 120
Naranja: 150

frutas = {
    "Banana": 80,
    "Manzana": 100,
    "Pera": 120,
    "Naranja": 150
}

fruta = input("Ingrese una fruta").capitalize()  # convierta la primera letra en mayúscula y el resto en minúsculas


if fruta in frutas:
    kilos = float(input("Ingrese la cantidad de kilos: "))
    precio = kilos * frutas[fruta]
    print(f"El precio de {kilos} kilos de {fruta} es {precio} pesos")
else:
    print("No ingresó una fruta de la lista")