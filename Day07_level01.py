#DAY 7 LEVEL 1

#>>>>>>>>>> PRIMERA PARTE <<<<<<<<<<<<<
# Ejercicio 1.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies)) #Output: 7

# Ejercicio 2.
it_companies.add('Twitter')

# Ejercicio 3.
it_companies.update(['Netflix' , 'Tesla' , 'Alibaba'])

# Ejercicio 4.
it_companies.remove('IBM') #Riases KeyError if IBM is not found 
# or
it_companies.discard('IBM') #No error if 'IBM' is not found 

#What is the difference bettwen remove and discard?
#remove() riases a KeyError if the element is not found in the set 
#discard() does not raise an errorif the element is not found


