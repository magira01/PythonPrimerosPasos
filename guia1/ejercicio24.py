#Ejercicio 24:
# Crear un programa que almacene el diccionario con los créditos de las 
# asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
# después muestre por pantalla los créditos de cada asignatura en el formato 
# <asignatura> tiene <créditos> créditos, donde <asignatura> 
# es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_cred = 0

for materia, credito in creditos.items():
    print(f"{materia} tiene {credito} créditos")
    total_cred += credito

print(f"El total de créditos es {total_cred}")