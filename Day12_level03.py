# >>>>>>>>>>>> DIA 12 LEVEL 03 <<<<<<<<

# 1. shuffle_list: devuelve una lista mezclada aleatoriamente
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled
print(shuffle_list([1, 2, 3, 4, 5]))  # Ejemplo: [3, 1, 5, 2, 4]

# 2. seven_unique_random_numbers: genera 7 números únicos entre 0 y 9
def seven_unique_random_numbers():
    return random.sample(range(10), 7)
print(seven_unique_random_numbers())  # Ejemplo: [1, 5, 0, 3, 8, 7, 6]
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return 'Invalid color type.'

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def seven_unique_random_numbers():
    return random.sample(range(10), 7)

import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return 'Invalid color type.'

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def seven_unique_random_numbers():
    return random.sample(range(10), 7)


