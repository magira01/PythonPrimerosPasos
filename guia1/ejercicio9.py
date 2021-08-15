#Ejercicio 9: 
# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por el peso
#de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
#en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Crear un programa que lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado. Mostrar el resultado por pantalla.

peso_p = 112 # gramos
peso_m = 75 # gramos

cant_p = int(input("Ingrese la cantidad de payasos de este pedido: "))
cant_m = int(input("Ingrese la cantidad de muñecas de este pedido: "))

peso_pqt = peso_p * cant_p + peso_m * cant_m # gramos



print(f"El peso total del paquete a enviar es {peso_pqt} gramos")
