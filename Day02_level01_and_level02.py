#Day 2: 30 days of python programing
## Level 1
first_name= "Allison Fernanda"
Last_Name= "Garcia Reyes"
country= "Mexico"
city= "Aguascalientes"
age= 18
is_married= False
skills = [ "HTML", "CSS", "JS", "REACT", "PYTHON" ]
personal_info = {
"Firstname": "Allison Garcia",
"Lastname": "Garcia Reyes",
"Country" : "Mexico",
"City" : "Aguascalientes"
}
#Level 2
print("------------------------------------------------------------------------------------------------------------------")
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ',Last_Name)
print('Last name length: ', len(Last_Name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', personal_info)
print("------------------------------------------------------------------------------------------------------------------")

print("first_name es un tipo de dato: ",type(first_name)) ## <Class 'str'>
print("Last_name es un tipo de dato: ",type(Last_Name)) ## <Class 'str'>
print("Country es un tipo de dato: ",type(country)) ## <Class 'str'>
print("City es un tipo de dato: ",type(city)) ## <Class 'str'>
print("Age es un tipo de dato: ",type(age)) ## <Class ''>
print("Is_married es un tipo de dato: ",type(is_married)) ## <Class 'Bool'>
print("Skills es un tipo de dato: ",type(skills)) ## <Class 'List'>
print("Personal_info es un tipo de dato: ",type(personal_info)) ## <Class 'Dict'>
print("------------------------------------------------------------------------------------------------------------------")


print("------------------------------------------------------------------------------------------------------------------")
print(len(first_name))
print(len(Last_Name))
print(len(country))
print(len(city))
print("------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------")
len_first=len(first_name)
len_last=len(Last_Name)

print("El nombre mas largo es: ", len_first > len_last) ##len_first(first name)> len_last(last name)
print("El apeido mas largo es: ", len_last> len_first) ##len_last(last name)> len_first(first name)
print("¿Tienen la misma longitud? ", len_first == len_last) ##len_first(first name) == len_last(last name)
print("------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------")
##Declaración de numeros°°
num_one=5
num_two=4

total= num_one + num_two  #9
diff=  num_one - num_two  #1
product= num_one * num_two #20
division= num_one / num_two #1.25
exp= num_one ** num_two     #625
remainder= num_one % num_two #1
floor_division= num_one // num_two #1
print("------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------")
##Área y circunferencia de un circulo°°
radio=30
pi=3.1416

areaCirculo= pi*radio**2
Cirfunferencia= 2*pi*radio

print("El área del circulo es de:  ",areaCirculo)
print("La circunferencia del circulo es de:  ",Cirfunferencia)
print("------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------")
##Radio como entrada de usuario
raidus=float(input("Ingrese el radio del circulo: "))
area= 3.1416 * raidus ** 2
print("El Área del circulo es: ", area)
print("------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------------------------------------------------------------------")
##Solicitar información al usuario
first_name = input("Ingresa tu primer nombre:  ")
Last_Name = input("Ingresa tu primer apeido:  ")
country = input("Ingresa tu país: ")
age = input("Ingresa tu edad: ")

help('Keywords') #help('Keywords')
