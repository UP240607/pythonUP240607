# >>>>>>>>>>>> Día 12 level 1 <<<<<<<<

# 1. list_of_hexa_colors: genera una lista de colores hexadecimales
def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

print(list_of_hexa_colors(3))  # ['#a3e12f', '#03ed55', '#eb3d2b']

# 2. list_of_rgb_colors: genera una lista de colores RGB
import random
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]
print(list_of_rgb_colors(3))  # Ejemplo de salida: ['rgb(123,45,67)', 'rgb(0,255,255)', 'rgb(100,100,100)']

# 3. generate_colors: generalizador para hexa o rgb
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return 'Invalid color type. Use "hexa" or "rgb".'

print(generate_colors('hexa', 2))
print(generate_colors('rgb', 3))


