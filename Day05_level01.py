#DAY 5 LEVEL 1

# 1. Declarar una lista vacía
empty_list=[]

# 2. Declarar una lista con más de 5 elementos
my_list=['Manzana', 'Banana', 'Naranja', 'Uva', 'Melón', 'Piña']

# 3. Obtener la lóngitud de la cadena
print('lóngitud de la lista llamada my_list: ',len(my_list))

# 4. Obtener el primer, medio y último elemento 
first_item=my_list[0]
middle_item=my_list[len(my_list)//2]
last_item=my_list[-1]

print('El primer elemento es:  ',first_item)
print('El elemneto del medio es:  ',middle_item)
print('El último elemento es:  ',last_item)

# 5. Declarar una lista llamada mixed_data_types
mixed_data_types=['Juan Perez', 30, 1.75, 'Soltero', 'Ciudad de méxico']
print('Lista de datos mixtos: ', mixed_data_types)

# 6. Declarar la lista it_companies
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir la lista
print('It Companies:  ', it_companies) 

# 8. Imprimir el número de compañías
print('Número de compañías:  ', len(it_companies))

# 9. Imprimir la primera, media y última compañía
print('La primera compañía:  ', it_companies[0])
print('La compañía del medio:  ', it_companies[len(it_companies)//2])
print('Última compañía:  ', it_companies[-1])

# 10. Módificar una compañía 
it_companies[1]= 'Alphabet'  #Google cambia a Alphabet
print('Despúes de modificar:  ', it_companies)

# 11. Agregar una compañía 
it_companies.append('Tesla')
print('Despues de agregar Tesla:  ', it_companies)

# 12. Insertar una compañía en el medio 
it_companies.insert(len(it_companies)//2, 'Netflix')
print('Después de insertar Netflix:  ', it_companies)

# 13. Cambiar un nombre a mayúsculas excepto (IBM)
it_companies[0]=it_companies[0].upper()
print('Con Facebook en mayúsculas:  ', it_companies)

# 14. Unir las campañas con '#; '
joined_companies = '#; '.join(it_companies)
print('Unidas con separador:  ', joined_companies)

# 15. Verificar si una compañía existe 
print('¿Esta Google en la lista?  ' in it_companies)

# 16. Ordenar la lista
it_companies.sort()
print('Ordenadas alfabéticamente:  ', it_companies)

# 17. Revertir la lista
it_companies.reverse
print('En orden descendente:  ', it_companies)

# 18. Cortar las primeras 3 compañías
print('Las primeras 3 compañías:  ', it_companies[:3])

# 19. Cortar las últimas 3 compañías
print('Últimas 3 compañías:  ', it_companies[-3:])

# 20. Cortar la(s) del medio
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
  print('Compañías del medio:  ', it_companies[middle_index-1:middle_index+1])
else:
  print('Compañía del medio:  ', it_companies[middle_index])

# 21. Eliminar la primera compañía
it_companies.pop(0)
print("Despúes de eliminar la primera:  ", it_companies)

# 22. Eliminar la del medio
middle_index = len(it_companies)//2
it_companies.pop(middle_index)
print('Después de eliminar la del medio:  ', it_companies)

# 23. Eliminar la última compañía
it_companies.pop()
print('Después de eliminar la última: ',it_companies)

# 24. Eliminar todas las compañías
it_companies.clear()
print("Después de eliminar todas:  ", it_companies)

# 25. Eliminar la lista por completo
del it_companies
# Aqui ya no se pone el print(it_companies) por que al poner eso automaticamente marca un error

# 26. Unir front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print('Full stack:  ', full_stack)

# 27. Insertar Python y SQL después de Redux
index = full_stack.index('Redux') + 1
full_stack[index:index] = ['Python', 'SQL']
print('Full stack actualizado:  ', full_stack)


