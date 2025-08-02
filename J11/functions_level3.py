"""Day11 30 days of Python Programming"""
###Exercices: Level 3
#1
import math
def is_prime(nb):
    sqrt = math.sqrt(nb)
    if int(sqrt) == (sqrt):
        return False
    for i in range(2, int(sqrt)):
        if nb%i == 0:
            return False
    return True

print("19 is prime: ", is_prime(19))


#2
def all_items_are_unique(lst: list):
    return len(set(lst)) == len(lst)

print("[2, 2, 0, 3, 4] has all items unique: ", all_items_are_unique([2, 2, 0, 3, 4]))
print("[1, 0, 3, 4] has all items unique: ", all_items_are_unique([1, 0, 3, 4]))


#3
def all_items_has_same_data_type(lst: list):
    type_lst = [type(i) for i in lst]
    type_lst = set(type_lst)
    return len(type_lst) == 1

print("All items are same data type:", all_items_has_same_data_type(["1", "2", '3']))

#4
def is_valid_var(st: str):
    valid_starts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    invalid = "@-#\"'([]){}+*/%^$;:!/.<>&"
    if st[0].upper() not in valid_starts:
        return False
    for i in range(1, len(st)):
        if(st[i]) in invalid:
            print("invalid", st[i])
            return False
    return True

print("_jkjfj^_hs is a valid variable", is_valid_var("jkjfj^_hs"))
print("my_var_1 is a valid variable", is_valid_var("my_var_1"))
print("_variable is a valid variable", is_valid_var("_variable"))



#5
##i

from country_data import get_country_data

countries_data = get_country_data()
def most_spoken_languages():
    langages = []
    for country in countries_data:
        langages += country.get("languages")
    apparition = {}
    for langage in langages:
        if not langage in apparition:
            apparition[langage] = langages.count(langage)

    apparition_sorted = dict(sorted(apparition.items(), key= lambda item: item[1], reverse=True))
    return list(apparition_sorted.keys())[:10]

print("Ten most spoken langages : ", most_spoken_languages())

##2
def most_populated_countries():
    country_sorted_by_population = sorted(countries_data, key= lambda country:country["population"], reverse=True)
    most_populated = []
    for ctr in country_sorted_by_population:
        most_populated.append(ctr["name"])
        if(len(most_populated) == 10):
            break

    return most_populated

print("Ten most populated countries : ", most_populated_countries())
