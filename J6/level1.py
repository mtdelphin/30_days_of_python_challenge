"""Day6 30 days of Python Programming"""
#Exercises: Level 1 
#1
empty_tpl = tuple()
#2
brothers=('Mathieu', 'Cader', 'Euphrem')
sisters=('Rose',  'Nicole')
#3
siblings=brothers+sisters
#4
print("I have {} siblings".format(len(siblings)))
#5
family_members = siblings+tuple(('Eric', 'Denise'))

#Exercises: Level 2 
#1
upck_siblings = family_members[:-2]
upck_parents = family_members[-2:]
#2
fruits=tuple(('mango', 'apple', 'avocado', 'lemon'))
vegetable=tuple(('cucumber', 'carrot', 'onions', 'ginger'))
animals=tuple(('chicken', 'beef', 'rabbit', 'fish'))
food_stuff_tp=fruits+vegetable+animals
#3
food_stuff_lt = list(food_stuff_tp)
#4
middle_item=food_stuff_lt[len(food_stuff_lt)//2]
#5
first_3_items=food_stuff_lt[:3]
last_3_items=food_stuff_lt[-3:]
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway','Sweden')

print("'Estonia' is a nordic country:", 'Estonia' in nordic_countries)
print("'Iceland' is a nordic country:", 'Iceland' in nordic_countries)

