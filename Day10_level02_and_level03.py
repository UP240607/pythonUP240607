# ==========================
# Ejercicios Nivel 2
# ==========================

# 1. Suma de números del 0 al 100
sum_total = 0
for i in range(101):
    sum_total += i
print("The sum of all numbers is", sum_total)

# 2. Suma de números pares e impares del 0 al 100
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is", sum_even, "And the sum of all odds is", sum_odd)


# ==========================
# Ejercicios Nivel 3
# ==========================

# 1. Países que contienen 'land' en su nombre
# Supongamos que countries.py define: countries = ['Finland', 'Iceland', ...]
from data.countries import countries  # adapta el import a tu estructura de archivos

lands = []
for country in countries:
    if 'land' in country.lower():
        lands.append(country)

print("Countries containing 'land':", lands)


# 2. Revertir la lista de frutas usando bucle
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruits:", reversed_fruits)


# 3. Uso de countries_data.py
from data.countries_data import countries_data

# 3.a. Número total de lenguajes en los datos (sin duplicados)
all_languages = set()
for country in countries_data:
    languages = country.get('languages', [])
    for lang in languages:
        all_languages.add(lang)

print("Total number of languages:", len(all_languages))

# 3.b. Diez idiomas más hablados (por número de países que lo usan)
lang_count = {}
for country in countries_data:
    for lang in country.get('languages', []):
        lang_count[lang] = lang_count.get(lang, 0) + 1

# ordenar por conteo y tomar los 10 primeros
top_10_languages = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("Ten most spoken languages:")
for lang, count in top_10_languages:
    print(f"{lang}: spoken in {count} countries")


# 3.c. Diez países más poblados
# datos asumen clave 'population'
pop_list = [(country['name'], country.get('population', 0)) for country in countries_data]
top_10_pop = sorted(pop_list, key=lambda x: x[1], reverse=True)[:10]
print("\nTen most populated countries:")
for name, pop in top_10_pop:
    print(f"{name}: population {pop}")
