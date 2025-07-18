# ==========================
# Ejercicios Nivel 2
# ==========================

# 1. Sistema de calificación
score = int(input("Ingresa tu puntaje (0-100): "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Puntaje inválido'

print("Tu calificación es:", grade)

# 2. Verificador de estación del año
month = input("Ingresa el mes: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    season = 'Otoño'
elif month in ['December', 'January', 'February']:
    season = 'Invierno'
elif month in ['March', 'April', 'May']:
    season = 'Primavera'
elif month in ['June', 'July', 'August']:
    season = 'Verano'
else:
    season = 'Mes inválido'

print("La estación es:", season)

# 3. Comprobador y modificador de lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Ingresa el nombre de una fruta: ").strip().lower()

if new_fruit in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(new_fruit)
    print("Lista de frutas actualizada:", fruits)
