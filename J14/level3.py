"""Day14 30 days of Python Programming"""

#Exercice level 3
from functools import reduce
from countries_data import get_countries_data

countries = get_countries_data()

#Sort countries by name, by capital, by population
countries_by_name = sorted(countries, key=lambda country: country["name"])
countries_by_capital = sorted(countries, key=lambda country: country["capital"])
countries_by_population=sorted(countries, key=lambda country: country["population"])


#Sort out the ten most spoken languages by location.
langages = reduce(lambda acc, lan: acc+lan, list(map(lambda country: country["languages"], countries)))
langages_unique = list(set(langages))
langages_apparition = sorted(list(map(lambda lang: (lang, langages.count(lang)), langages_unique)), key=lambda lang: lang[1], reverse=True)
ten_most_spoken = list(map(lambda x: x[0], langages_apparition[:10]))

#Sort out the ten most populated countries.
ten_most_populated_countries = countries_by_population[-10:][::-1]
print(ten_most_populated_countries)