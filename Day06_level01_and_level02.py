##DIA 6 LEVEL 1 Y 2

#>>>>>>>>> PRIMER NIVEL <<<<<<<<<<
# Ejercicio 1.
emty_tuple = ()

#Ejercicio 2.
brothers = ('John' , 'Mike')
sisters = ('Emily' , 'Sarah')

#Ejercicio 3.
siblings = brothers + sisters

# Ejercicio 4.
num_siblings = len(siblings)
print(num_siblings) #Output: 4

#Ejercicio 5.
father = 'Robert'
mother = 'Mary'
family_members = siblings + (father , mother )

#>>>>>>>> SEGUNDO NIVEL <<<<<<<<<<<<<

# Ejercicio 1.
*siblings, father, mother = family_members
print(siblings) #Output: ['John' , 'Mike' , 'Emily' , 'Sarah']
print(father) #Output: 'Robert'
print(mother) #Output: 'Mary'

#Ejercicio 2.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot' , 'potato' , 'spinach')
animal_products = ('milk' , 'meats' , 'eggs')
food_stuff_tp = fruits + vegetables + animal_products

#Ejercicio 3.
food_stuff_it = list(food_stuff_tp)

# Ejercicio 4.
middle_index = len(food_stuff_it) // 2
middle_item = food_stuff_it[middle_index]
print(middle_item) #Output: 'spinach'  (assuming 9 items)

#Ejercicio 5.
first_three = food_stuff_it[:3]
last_three = food_stuff_it[-3:]
print(first_three)  #Output: ['apple', 'banana', 'orange']
print(last_three)  #Output: ['milk', 'meat', 'eggs']

#Ejercicio 6.
del food_stuff_tp 

# Ejercicio 7.
nordic_countries = ('Denmark' , 'Finland' , 'Iceland' , 'Norway' , 'Sweden')
print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries) #Output: True
