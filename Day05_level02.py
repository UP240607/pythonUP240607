# DIA 5 LEVEL 1

#>>>>>>  Primera parte:  <<<<<<  
# Edades de estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24 ]

# 1. Ordenar la lista y encontrar max y min 
ages.sort()
min_age = min(ages)
max_age = max(ages)
print('Edades ordenadas:  ', ages)
print('Edad mínima:  ', min_age)
print('Edad máxima:  ', max_age) 

# 2. Agregar min y max edad otra vez a la lista 
ages.append(min_age)
ages.append(max_age)
print('Lista después de agregar min y max otra vez:  ', ages)

# 3. Encontrar la edad mediana
ages.sort()
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2-1] + ages[n//2])/2
else: 
    median_age = ages[n//2]
print('Edad mediana:  ', median_age)

# 4. Promedio de edades
average_age = sum(ages) / len(ages)
print('Edad promedio:  ', average_age)

# 5. Rango de edades ( max - min )
range_age = max_age - min_age
print('Rango de edades:  ', range_age)

# 6. Comparar |min - promedio| y |max - promedio|
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print('|min - promedio|:  ', min_diff)
print('|max - promedio|:  ', max_diff)


#>>>>>>>>  Seguna parte   <<<<<<<
# Lista de países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# 7. Encontrar el país del medio (o los países del medio)
n = len(countries)
if n % 2 == 0:
    middle_countries = countries[n//2-1: n//2+1]
else: 
    middle_countries = [countries[n//2]]
print('País(es) del medio:  ', middle_countries)

# 9. Dividir la lista en dos partes iguales (o casi iguales)
if n % 2 == 0: 
    first_half = countries[:n//2]
    second_half = countries[n//2:]
else:
    first_half = countries[:n//2 + 1]
    second_half = countries[n//2+ 1:]
print('Primera mitad:  ', first_half)
print('Segunda mitad:  ', second_half)

# 9. Desempaquetar primeros tres países, el resto como 'scandic_countries'
china, russia, usa, *scandic_countries = countries
print('China:  ', china)
print('Russia:  ', russia)
print('USA:  ', usa)
print('Países escandinavos:  ', scandic_countries)
