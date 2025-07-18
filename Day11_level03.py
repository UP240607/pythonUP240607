#>>>>>>>>>>>>>>>>>>>> DIA 11 level 3 <<<<<<<<<<<<<<<<<<<

# 1. is_prime: checks if a positive integer is prime
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 2. all_unique: checks whether all items in a list are unique
def all_unique(lst) -> bool:
    return len(set(lst)) == len(lst)

# 3. all_same_type: checks if all items have the same type
def all_same_type(lst) -> bool:
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(x) is first_type for x in lst)

# 4. is_valid_variable: checks if a string is a valid Python identifier and not a keyword
import keyword
import re

def is_valid_variable(name: str) -> bool:
    return bool(re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name)) and not keyword.iskeyword(name)

# Sample structure inside countries-data.py:
# countries = [
#     {"name": "China", "population": 1402112000, "languages": ["Chinese"]},
#     {"name": "India", "population": 1366417754, "languages": ["Hindi", "English"]},
#     ...
# ]
## from countries_data import countries
from collections import Counter

def most_spoken_languages(countries, top_n=10):
    lang_counter = Counter()
    for country in countries:
        for lang in country.get("languages", []):
            lang_counter[lang] += 1
    return lang_counter.most_common(top_n)

def most_populated_countries(countries, top_n=10):
    sorted_c = sorted(countries, key=lambda c: c.get("population", 0), reverse=True)
    return [(c["name"], c["population"]) for c in sorted_c[:top_n]]

