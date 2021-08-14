#Ejercicio 7: 
# Crear un programa que pida al usuario dos números enteros 
# y muestre por pantalla la división de <n> en <m> 
# da un cociente <c> y un resto <r> 
# donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la
#división entera respectivamente.

n = int(input("Intruduce un num entero: n= "))
m = int(input ("Introduce un segundo numero entero: m= "))

cociente, resto = n// m, n % m 
# declaro la variable cociente y resto antes del = 
#y luego realizo la operatoria utilizando // para cociente y % para resto

print(f"La división entre {n} y {m} da un cociente {cociente} y un resto {resto}")
