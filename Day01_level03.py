## Ejercicio 3

#Number types
interger_num = 10
float_num = 3.14
complex_num = 4+5j

print("Interger: ", interger_num) 
print("Float: ", float_num) 
print("Complex: ", complex_num) 
print( [1,2,3]) #STRING

#String
name = 'Fernanda'
print("String: ", name)

#Boolean
is_student = True
print("Boolean:  ", is_student)

#List
languajes = ["Python", "JavaScript", "C++"]
print("list: ", languajes )

#Tuple
cordinates = (10,20)
print("Tuple: ", cordinates)

#set
unique_numbers = { 1, 2, 3, 3, 2 }
print("Set: ", unique_numbers)

#Dictionary
mi_diccionario = {
    "nombre": "Allison",
    "edad": 18,
    "ciudad": "Mexico"
}
print("Dictionary:  ", mi_diccionario)



import math

# Coordenadas de los puntos
punto1 = (2, 3)
punto2 = (10, 8)

# Cálculo de la distancia euclidiana
distancia = math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)

print("La distancia euclidiana es:  ", distancia)