#DAY 7 LEVEL 2
#>>>>>>>>>>>  SEGUNA PARTE <<<<<<<<<<<<<<<<<<<<<

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicio 1.
A.union(B) # or A | B Output: { 19, 20, 22, 24, 25, 26, 27, 28 }

#Ejercicio 2.
A.intersection(B) # or A & B Output: { 19, 20, 22, 24, 25, 26 }

#Ejercicio 3.
A.issubset(B) # or A <= B Output: True

#Ejercicio 4.
A.isdisjoint(B) # False 

#Ejercicio 5.
A.update(B) # Joins B into A ( modifies A )
B.update(A) # Joins A into B ( modifies B )

#Ejercicio 6.
A.union(B) # A | B
B.union(A) # B | A ( Same result as A | B)

#Ejercicio 7.
A.symmetric_difference(B) # or A ^ B Output: { 27, 28 }

#Ejercicio 8.
del A
del B






