# >>>>>>>>>>>>> Level 1 Día 11 <<<<<<<<<<<<<<<<

# 1.Ejercicio
def add_two_numbers (a, b):
    return a + b

# 2.Ejercicio
def area_of_circle(r):
    pi=3.14159
    return pi*r*r

# 3.Ejercicio
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All elements must be numbers"

# 4.Ejercicio
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 5.Ejercicio
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    return 'Invalid month'

# 6.Ejercicio
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Infinity'
    return (y2 - y1) / (x2 - x1)


# 7.Ejercicio
import math
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No real solutions'
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

# 8.Ejercicio
def print_list(lst):
    for item in lst:
        print(item)


# 9.Ejercicio
def reverse_list(lst):
    reversed_list = []
    for item in reversed(lst):
        reversed_list.append(item)
    return reversed_list

# 10.Ejercicio
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# 11.Ejercicio
def add_item(lst, item):
    lst.append(item)
    return lst

# 12.Ejercicio
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13.Ejercicio
def sum_of_numbers(n):
    return sum(range(n + 1))


# 14.Ejercicio
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)


# 15.Ejercicio
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
