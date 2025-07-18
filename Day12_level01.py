# >>>>>>>>>>>>> DIA 12 level01

# 1. random_user_id: Genera un ID aleatorio de 6 caracteres
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())  # Ejemplo: 'aK92jF'

# 2. user_id_gen_by_user: genera múltiples IDs con longitud personalizada
def user_id_gen_by_user():
    chars = int(input("Enter number of characters per ID: "))
    count = int(input("Enter number of IDs to generate: "))
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=chars)) for _ in range(count)]
    return '\n'.join(ids)

# print(user_id_gen_by_user())

# 3. rgb_color_gen: genera un color RGB aleatorio
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())  # Ejemplo: rgb(120, 34, 255)

