# >>>>>>>>>>>> DIA 13 LEVEL 01 <<<<<<<<<<<<<<<<
#Datos: = [-4, -3, -2, -1, 0, 2, 4, 6]  filtered = [n for n in numbers if n <= 0]  print(filtered)  # [-4, -3, -2, -1, 0]

# 1. Filtramos los números negativos y ceros de una lista usando list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if n <= 0]
print(filtered)  # [-4, -3, -2, -1, 0]

# 2. Aplanamos list_of_lists para que todos los números estén en una sola lista
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Creamos una lista de tuplas donde cada tupla contiene potencias del número del 0 al 10
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)
# Ejemplo: (2, 1, 2, 4, 8, 16, 32)

# 4. Convertimos cada país a una lista: [PAIS, CODIGO (3 letras), CAPITAL] todo en mayúsculas
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for [[(country, city)]] in countries]
print(output)
# [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Convertimos cada país a un diccionario con claves 'country' y 'city'
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dicts = [{'country': country.upper(), 'city': city.upper()} for [[(country, city)]] in countries]
print(dicts)
# [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]

# 6. Convertimos tuplas de nombres a un solo string como 'Nombre Apellido'
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[(first, last)]] in names]
print(full_names)
# ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7A. Calculamos la pendiente (m) dados dos puntos (x1, y1), (x2, y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
print(slope(1, 2, 3, 6))  # Resultado: 2.0

# 7B. Calculamos la intersección en Y (b) dado un punto y la pendiente
y_intercept = lambda x, y, m: y - m * x
print(y_intercept(3, 6, 2))  # Resultado: 0

