# ==========================
# Ejercicios Nivel 3
# ==========================

# Diccionario de persona
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Verificar si existe la clave 'skills' y mostrar la habilidad del medio
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Habilidad del medio:", skills[middle_index])

# 2. Verificar si la persona tiene la habilidad 'Python'
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("¿Tiene Python?", has_python)

# 3. Clasificación según habilidades
if 'skills' in person:
    skills_set = set(person['skills'])

    if skills_set == {'JavaScript', 'React'}:
        print('Es un desarrollador Frontend.')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('Es un desarrollador Backend.')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('Es un desarrollador Fullstack.')
    else:
        print('Título desconocido.')

# 4. Verificar si está casado y vive en Finlandia
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} vive en Finlandia. Está casado.")
