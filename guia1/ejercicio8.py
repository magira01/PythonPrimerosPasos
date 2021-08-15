#Ejercicio 8: 
# Crear un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la
#inversión.

inv = float(input("Ingrese la cantidad que desea invertir: "))
int_anual = float(input("Ingrese el interés anual: "))
n = int(input("Ingrese la cantidad de años de la inversión: "))

if int_anual >= 1:
    int_anual /= 100 
# aqui la logica del if es: si un el usuario ingresa un interes menor a 1 
# lo toma el valor tal cual lo ingresa, sino lo divide en 100, para poder hacer la cuenta.
    
capital_obtenido = inv + inv * int_anual * n
print(f"El capital obtenido es {capital_obtenido}")