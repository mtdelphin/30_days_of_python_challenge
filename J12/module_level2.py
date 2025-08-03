"""Day12 30 days of Python Programming"""
from string import ascii_letters, digits
import random
from module_level1 import rgb_color_gen
#Exercices: Level2
#1
def generate_hexa_colors():
    color="#"
    base=digits+"abcdef"
    for i in range(6):
        color+=base[random.randint(0, len(base)-1)]
    return color

def list_of_hexa_colors(nb):
    for i in range(nb):
        print(generate_hexa_colors())

list_of_hexa_colors(3)


def list_of_rgb_colors(nb):
    return [rgb_color_gen() for i in range(nb)]

# python3 J12/module_level2.py 6 1
print(list_of_rgb_colors(2))


#3
def generate_colors(mod, nb):
    if mod=='hexa':
        return [generate_hexa_colors() for i in range(nb)]
    return list_of_rgb_colors(nb)

print(generate_colors('hexa', 2))
print(generate_colors('rgb', 2))