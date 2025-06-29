# Day 07 Level 3
#>>>>>>>>>> TERCERA PARTE <<<<<<<<<<<<<<<<<

age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicio 1.
age_set = set(age)
len(age) #8
len(age_set) # 5 ( Since duplicates are removed )

#String: Immutable sequence of characters, e.g., "hello".
#List: Mutable ordered sequence of elements, e.g., [1, 2, 3].
#Tuple: Immutable ordered sequence of elements, e.g., (1, 2, 3).
#Set: Mutable unordered collection of unique elements, e.g., {1, 2, 3}.

#Ejercicio 2. 
sentence = " I am a teacher and I love to inspire and teach people "
words = sentence.split () # Split into list of words
unique_words = set(words) # Convert to set to remove duplicated unique words: \n {'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people'}) 
len(unique_words) #Number of unique words Output: 10 