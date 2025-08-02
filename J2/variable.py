#Jour 2 30 days of Python Programming
"""Niveau 1"""
first_name="Frank"
last_name="MPO"
full_name="Patrice TALON"
country_city=("Benin", "Cotonou")
year=2025
is_married=False
is_true=True
is_light=False
category, brand, model, release_year, specs,  = "super bike", "Honda", "CBR 1000RR-R", "2024", {"motor": ["inline 4 cylinder", "999 cc", "double act", "16 valves", "220 Hp"], "security": "ABS, brembo brake"}


"""Niveau 2"""
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country_city))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(category), type(brand), type(model), type(release_year), type(specs))

print(len(first_name))
print(len(last_name)) #le nom est plus court que le prenom

num_one, num_two = 5, 4
sum_num = sum([num_one, num_two])
substract=num_two - num_one
product = num_one * num_two
division=num_one/num_two
rest=num_one%num_two
floor_rest = num_one//num_two

print("sum: ", sum_num)
print("substract: ", substract)
print("product: ", product)
print("division: ", division)
print("rest: ", rest)
print("floor_rest: ", floor_rest)



circle_radius = 30
area_of_circle = (circle_radius**2)*3.14
circum_of_circle = circle_radius*2*3.14
print("area of circle: ", area_of_circle)
print("circum of circle: ", circum_of_circle)

circle_radius = input("Entrez le rayon: ")
print("area value: ", (int(circle_radius)**2)*3.14)


first_name = input("Entrez votre prenom: ")
last_name = input("Entrez votre nom: ")
cpuntry = input("Entez votre pays: ")
age = input("Entez votre age: ")


help('keywords')
