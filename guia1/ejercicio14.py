#Ejercicio 14:
#  En una determinada empresa, sus empleados son evaluados 
# al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 
# y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 100000 multiplicada por la puntuación del nivel.
#Nivel Puntuación
#Inaceptable 0.0
#Aceptable 0.4
#Meritorio 0.6 o más
#Crear un programa que lea la puntuación del usuario e indique su nivel de rendimiento,
#así como la cantidad de dinero que recibirá el usuario.

punt_us = float(input("Ingrese la puntuación obtenida: "))
bonif = punt_us * 100000

if punt_us == 0.0:
    bonif *= punt_us
    print(f"Rendimiento inaceptable, recibe {bonif} pesos")
elif punt_us == 0.4:
    bonif *= punt_us
    print(f"Rendimiento aceptable, recibe {bonif} pesos")
elif punt_us >= 0.6:
    bonif *= punt_us
    print(f"Rendimiento meritorio, recibe {bonif} pesos")
else:
    print("No ingresó una puntuación correcta")