#TRABAJO 1---
print(3 + 4)   
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 ** 4)
print(3 % 4)
print(3 // 4)

print(type('ALLISON'))
print(type('GARCIA'))
print(type('MEXICANA'))
print(type('10'))
print(type('9.8'))
print(type('3.14'))
print(type('4-4J'))
print(type('ASABENEH'))
print(type('Phyton'))
print(type('Finlandia'))

## EJERCICIO 2
print('Hello my beautiful people')
print(3 + 4)   
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 ** 4)
print(3 % 4)
print(3 // 4)

print('ALLISON')
print('GARCIA')
print('MEXICANA')
print('10')
print('9.8')
print('3.14')
print('4-4J')
print('ASABENEH')
print('Phyton')
print('Finlandia')

## Ejercicio 3
print(10) #INT
print(2.6) #FLOAT
print(6 + 3j) #COMPLEX
print( [1,2,3]) #STRING

a=True
b=False
print(a) #Salida:True
print(b) #Salida:False
print( 9.8, 3.14, 2.7 ) #TUPLE
mi_diccionario = {
    "nombre": "Allison",
    "edad": 18,
    "ciudad": "Mexico"
}

# Acceder a un valor
print(mi_diccionario["nombre"])  # Allison

# Agregar o modificar valores
mi_diccionario["edad"] = 18

# Eliminar una clave
del mi_diccionario["ciudad"]

# Recorrer un diccionario
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)

import math

# Coordenadas de los puntos
punto1 = (2, 3)
punto2 = (10, 8)

# Cálculo de la distancia euclidiana
distancia = math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)

print("La distancia euclidiana es:", distancia)



