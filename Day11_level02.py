# >>>>>>>>>>>>> Level 2 Día 11 <<<<<<<<<<<<<<<<

# 1. evens_and_odds: counts digits that are even vs. odd in a positive integer
def evens_and_odds(n: int):
    evens = odds = 0
    for ch in str(n):
        digit = int(ch)
        if digit % 2 == 0:
            evens += 1
        else:
            odds += 1
    return odds, evens

# Usage example:
o, e = evens_and_odds(100)
print(f"The number of odds are {o}.")
print(f"The number of evens are {e}.")


# 2. factorial: computes n!
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 3. is_empty: checks if a given parameter is "empty"
def is_empty(x) -> bool:
    try:
        return len(x) == 0
    except TypeError:
        # Not a sequence/type that supports len()
        return False

# 4. Statistical functions on lists
import math
from collections import Counter
from statistics import mean

def calculate_mean(lst):
    return mean(lst)

def calculate_median(lst):
    n = len(lst)
    s = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]

def calculate_mode(lst):
    c = Counter(lst)
    max_freq = max(c.values())
    modes = [k for k, v in c.items() if v == max_freq]
    if len(modes) == len(c):
        return None  # all values appear once – no clear mode
    return modes

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst, sample=True):
    mu = calculate_mean(lst)
    n = len(lst)
    ssd = sum((x - mu) ** 2 for x in lst)
    return ssd / (n - 1) if sample and n > 1 else ssd / n

def calculate_std(lst, sample=True):
    return math.sqrt(calculate_variance(lst, sample))
