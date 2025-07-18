# 1. Check driving eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year{'s' if years_left > 1 else ''} to learn to drive.")

# 2. Compare your age with my_age
my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

# 3. Compare two numbers
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
