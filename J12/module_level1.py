"""Day12 30 days of Python Programming"""
from string import ascii_letters, digits
import random
import sys
#Exercices: Level1
#1
def random_user_id(ln=6):
    base = ascii_letters+digits
    id=""
    for i in range(ln):
        id+=base[random.randint(0, len(base)-1)]
    return id

print(random_user_id())


#2
def user_id_gen_by_user():
    ln=int(sys.argv[1])
    nb=int(sys.argv[2])

    for i in range(nb):
        print(random_user_id(ln))

#python3 J12/module_level1.py  16 5
user_id_gen_by_user()

#3
def rgb_color_gen():
    return "rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print(rgb_color_gen())