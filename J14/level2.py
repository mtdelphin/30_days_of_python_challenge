"""Day14 30 days of Python Programming"""
import functools
#Exercices level2

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1
uppercase = lambda x: x.upper()

countries_upper = map(uppercase, countries)

print(list(countries_upper))

#2
def square(x):
    return x**2

numbers_squarred = map(square, numbers)
print(list(numbers_squarred))

#3
names_upper=map(uppercase, names)
print(list(names_upper))

#4
def land_in(string):
    return "land" in string

countries_land = filter(land_in, countries)
print(list(countries_land))

#5
def six_character(x):
    return len(x)==6

countries_6_char = filter(six_character, countries)
print(list(countries_6_char))

#6
def six_more_char(x):
    return len(x) >= 6
countries_6_more_char = filter(six_more_char, countries)
print(list(countries_6_more_char))

#7
def starts_with_E(x: str):
    return x.startswith("E")

countries_starts_E = filter(starts_with_E, countries)
print(list(countries_starts_E))

#8
def split_str(t, current):
    return t+current

countries_six_more_char_starts_E = functools.reduce(split_str, list(map(uppercase, list(filter(land_in, countries)))))
print(countries_six_more_char_starts_E)


#9
def get_string_lists(items: list):
    return list(filter(lambda x: type(x) == str, items))

print(get_string_lists([1, "s", "b", {1, 3}, ["1"], 4, False, "l"]))

#10
def sum_items(x, y):
    return x+y

sum_numbers = functools.reduce(sum_items, numbers)
print(sum_numbers)

#11
def concatenate(x, y):
    if len(x.split(",")) <= len(countries) -2:
        return x+", "+y
    else:
        return x+" and "+y

concatened = functools.reduce(concatenate, countries)
print(concatened+" are north European countries")

#12
from countries import get_countries

countries = get_countries()

patterns = ['land', 'ia', 'island', 'stan']

def categorize_countries():
    f_countries = []
    for pattern in patterns:
        def filter_countries(value):
            return pattern in value.lower()
        
        cat = filter(filter_countries, countries)
        f_countries.append(list(cat))

    return f_countries

print(categorize_countries())

#13
def _join_dict(acc: dict, x: dict):
    acc.update(x)
    return acc


def dct_letter():
    letters = list(map(lambda country: country[0], countries))
    uniq_letter=set(letters)
    counts=functools.reduce(_join_dict, list(map(lambda l: {l: letters.count(l)}, uniq_letter)))
    return counts

print(dct_letter())

#14
def get_first_ten_countries():
    return countries[:10]
print(get_first_ten_countries())

def get_last_ten_countries():
    return countries[-10:]

print(get_last_ten_countries())
