# DAY 8 LEVEL 1
#>>>>>>>>> Primera Parte <<<<<<<<<<<<<<<<

# 1. Create an empty dicotionary called dog 
dog = {}

# 2. Add name, color, breed, leg, age to the dog dictionary
dog['name'] = "Budy"
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = '4'
dog['age'] = '5'

# 3. Create a student dictionary and add keys
student = {
    'First name':'Jhon',
    'Last name': 'Doe',
    'Gender':'Male',
    'Age': 21,
    'Marital_status': 'Single',
    'Skills': ['Python' , 'Data Analysis'], 
    'Country': 'USA', 
    'City':'New York',
    'Address': '123 Main St'
}

# 4. Get the length of the student dictionary
student_lenght = len(student)
print('Lenght of students dictionary: ', student_lenght)

# 5. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Type of skills:", type(skills))  # Should be <class 'list'>

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Machine Learning')
student['skills'].append('SQL')
print("Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("Values:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student items (tuples):", student_items)

# 10. Delete one of the items in the dictionary
del student['marital_status']
print("After deleting 'marital_status':", student)

# 11. Delete one of the dictionaries
del dog
# Trying to print 'dog' now would raise an error because it's deleted



