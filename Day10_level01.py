# ==========================
# Ejercicios Nivel 1
# ==========================

# 1. Iterar del 0 al 10 con for loop
print("For loop (0 al 10):")
for i in range(11):
    print(i)

# 2. Iterar del 0 al 10 con while loop
print("\nWhile loop (0 al 10):")
i = 0
while i <= 10:
    print(i)
    i += 1

# 3. Iterar del 10 al 0 con for loop
print("\nFor loop (10 al 0):")
for i in range(10, -1, -1):
    print(i)

# 4. Iterar del 10 al 0 con while loop
print("\nWhile loop (10 al 0):")
i = 10
while i >= 0:
    print(i)
    i -= 1

# 5. Triángulo con 7 líneas
print("\nTriángulo:")
for i in range(1, 8):
    print('#' * i)

# 6. Cuadro 8x8 con #
print("\nCuadro 8x8:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 7. Tabla de multiplicar 0 al 10
print("\nTabla de multiplicar:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 8. Iterar lista de tecnologías
print("\nLista de tecnologías:")
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tech_list:
    print(tech)

# 9. Imprimir números pares del 0 al 100
print("\nNúmeros pares del 0 al 100:")
for i in range(101):
    if i % 2 == 0:
        print(i)

# 10. Imprimir números impares del 0 al 100
print("\nNúmeros impares del 0 al 100:")
for i in range(101):
    if i % 2 != 0:
        print(i)
