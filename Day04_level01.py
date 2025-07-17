## 1. DIA 4

# 1. Concatenar 'Thirty', 'Days', 'of', 'Python' 
concatened1='Thirty' + 'Days' + 'Of' + 'Python'
print(concatened1)

# 2. Concatenar 'Coding', 'For', 'All'
concatened2= 'Coding' + 'For' + 'All'
print(concatened2)

# 3. Declarar Variable Company
company = "Coding for all"

# 4. Imprimir variable company
print(company)

# 5. Imprimir Longitud de company
print(len(company))

# 6. Convertir a mayúsculas 
print(company.upper())

# 7. Convertir a minúsculas 
print(company.lower())

# 8. Capitalize()
print(company.capitalize())

# 9. Title  
print(company.title())

# 10. swapcase()
print(company.swapcase())

# 11. Cortar la primera palabra
print(company[7:])

# 12. Verificar si contiene la palabra "Coding"
print('Coding' in company) #True
print(company.index('Coding')) #0
print(company.find('Coding')) #0

# 13. Reemplazar "Coding" por "Python" 
print(company.replace('Coding', 'Python'))

# 14. Reemplazar "Everyone" por "All"
print('Python for everyone'.replace('Everyone', 'All'))

# 15. Dividir 'Coding For All'
print(company.split())

# 16. Dividir por coma 
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split())

# 17. Carácter en índice 0
print(company[0]) 

# 18. Último Índice 
print(company[-1])

# 19. Carácter en índice 10
print(company[10])

# 20. Acrónico 'Pyhton For Everyone'
phrase1 = 'Python For Everyone'
acronym1 = ''.join([word[0] for word in phrase1.split()])
print(acronym1)

# 21. Acrónimo 'Coding For All'
phrase2 = 'Coding For All'
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym2)

# 22. Posición de primera C 
print(company.index('C'))

# 23. Posición de primera F 
print(company.index('F'))

# 24. Última aparición de 'l' usando rfind
print('Coding For All People'.rfind('1'))

# 25. Primera ocurrencia de 'because'
sentence = 'You cannot end a sentence whit because because because is a conjunction'
print(sentence.find('because'))

# 26. Última ocurrencia de 'because' con rindex 
print(sentence.rindex('because')) 

# 27. Cortar 'because because because' 
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# 28. Igual al 25 (repetido para práctica)
print(sentence.find('because'))

# 29. Igual al 27 (repetido para práctica)
print(sentence[start:end])

# 30. ¿Empieza con 'Coding'?
print(company.startswith('Coding'))

# 31. ¿Termina con 'Coding'?
print(company.endswith('Coding'))

# 32. Quita espacios al inicio y al fin
print('       Coding For All            '.strip())

# 33. ¿Cuál es un identificador válido? 
print('30DaysOfPytho'.isidentifier())   #False

# 34. Lista de librerias unidas con #
Libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(Libraries))

# 35. Usar nueva línea (\n) 
print('I am enjoying this challenge.\nI just wonder what is next')

# 36. Usar tabulaciones (\t)
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t18\tFinland\tHelsinki')

# 37. Área de un círculo 
radio = 10
area = 3.14 * radio ** 2
print("The área of a circle with radius {} is {:.0f} meters square. ".format(radio, area))

# 38. Operaciones matemáticas con formato
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

