## Day 3

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 1. Declarar variables 
age=23
height= 1.75
complex_number= 2+3j


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 2. Área de un tiangulo 
base=float(input("Ingrese la base del triangulo: "))
altura=float(input("Ingrese la altura del triangulo: "))
AreaDelTriangulo= (base*altura)/2
print("El área del triangulo es de:  ",AreaDelTriangulo)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 3. Perímetro de un triángulo

lado_a=float(input("Ingrese el lado A del triángulo: "))
lado_b=float(input("Ingrese el lado B del triangulo:  "))
lado_c=float(input("Ingrese el lado C del triangulo:  "))
perimetro=lado_a+lado_b+lado_c
print("El perímetro del triangulo es de:  ", perimetro)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 4. Área y perimetro de un rectángulo

longitudAR=float(input("Ingresa la longitud del rectángulo: "))
anchoAR=float(input("Ingresa el ancho del rectángulo:  "))
areaRectangulo=longitudAR*anchoAR
perimetroR=2*(longitudAR+anchoAR)
print("Área del rectángulo:  ", areaRectangulo)
print("Perímetro del rectángulo:  ",perimetroR)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 5.Área y circunferencia de un circulo

radioC=float(input("Ingresa el radio del círculo:  "))
pi= 3.14 #Tipo float
AreaCirculo=pi*radioC**2
circunferenciaC=2*pi*radioC
print("El área del círculo es de:  ",AreaCirculo)
print("La circunferencia del círculo es de:  ",circunferenciaC)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 6. Ecuación: y = 2x - 2
pendiente_funcion = 2
intercepto_y = -2
intercepto_x = (0 + 2) / 2  # cuando y = 0 => x = 1
print("La pendiente (slope) es:", pendiente_funcion)
print("El intercepto en y (cuando x=0) es:", intercepto_y)
print("El intercepto en x (cuando y=0) es:", intercepto_x)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 7.Pendiente y distancia entre dos puntos 
x1,y1=2,2
x2,y2=6,10
pendiente=(y2 - y1) / ( x2 - x1 )
distancia=((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Pendiente entre (2,2) y (6,8):  ",pendiente)
print("Distancia eucladiana:  ",distancia)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 8. Comparar pendientes 
pendiente_funcion = 2
pendiente_puntos = (10 - 2) / (6 - 2)

print("Pendiente de y = 2x - 2:", pendiente_funcion)
print("Pendiente entre (2, 2) y (6, 10):", pendiente_puntos)

if pendiente_funcion == pendiente_puntos:
    print("✅ Ambas pendientes son iguales.")
else:
    print("❌ Las pendientes son diferentes.")



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 9. Ecuación y = x² + 6x + 9
print("Solución de y = x² + 6x + 9 para distintos valores de x:")
for x in range(-5, 1):  # valores desde -5 hasta 0
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
print("y es 0 cuando x = -3 (raíz de la ecuación)")



print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 10. Comparación de longitud
print(len("python") != len("dragon"))  # True


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 11. Verificar si 'on' está en ambas palabras
print('on' in 'python' and 'on' in 'dragon')  # True


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 12. Verificar si 'jargon' está en la oración
oracion = "I hope this course is not full of jargon"
print('jargon' in oracion)  # True


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 13. Negación de 'on' en ambas
print(not ('on' in 'dragon' and 'on' in 'python'))  # False


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 14. Longitud de 'python' a float y a string
largo_python = len("python")
print(float(largo_python))  # 6.0
print(str(largo_python))    # "6"


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 15. Verificar si un número es par
numero = int(input("Ingresa un número para verificar si es par: "))
print(numero % 2 == 0)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 16. División entera y comparación
print(7 // 3 == int(2.7))  # True

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 17. 1o equal to type 10
print(type('10') == type(10))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 18. int('9.8') genera error, así que usamos float primero
print(int(float('9.8')) == 10)  # False


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 19. Calcular pago semanal
print("\n--- Punto 19 ---")
horas = float(input("Ingresa las horas trabajadas: "))
tasa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tasa
print("Tu ganancia semanal es:", salario)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 20. Segundos vividos
print("\n--- Punto 20 ---")
anios = int(input("¿Cuántos años has vivido?: "))
segundos = anios * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# 21. Tabla de potencias
print("\n--- Punto 21: Tabla de potencias ---")
print("N  N^0 N^1 N^2 N^3")
for i in range(1, 6):
    print("{:<2} {:<3} {:<3} {:<3} {:<3}".format(i, 1, i, i**2, i**3))

# 22. ingresar años vividos, calcular segundos vividos
años = int(input("¿Cuántos años has vivido?: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Has vivido por {segundos} segundos.")


# 23. Escriba un script en Python que muestre la siguiente tabla
Ejemplo_tabla="""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print(f"Escriba un script en Python que muestre la siguiente tabla : \n\n {Ejemplo_tabla} \n")
for i in range(1, 6):
    print(f"{i} {1} {i} {i*2} {i*3}")

