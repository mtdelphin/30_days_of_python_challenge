"""Day19 30 days of Python Programming"""

from functools import reduce
import json
import re

#1

def count_lines_and_words(file_path):
    try:
        with open(file_path) as f:
            content=f.read()
            lines=content.splitlines()
            print(f"Number of lines in '{file_path}' : ", len(lines))
            print(f"Number of words in '{file_path}' : ", len(re.findall(r"\w+", content)))
    except Exception as e:
        print("An error occured getting lines: ", e)
    
# a
count_lines_and_words("./data/obama_speech.txt")
#b
count_lines_and_words("./data/michelle_obama_speech.txt")
#c
count_lines_and_words("./data/donald_speech.txt")
#d
count_lines_and_words("./data/melina_trump_speech.txt")

#2
def most_spoken_languages(filename, limit):
    with open(filename) as f:
        countries=json.load(f)
        langages=reduce(lambda langs, item, : langs+item, map(lambda country: country.get("languages"), countries))
        langages_unique=set(langages)
        appearences=[(langages.count(lang), lang) for lang in langages_unique]
        return sorted(appearences, key=lambda lang: lang[0], reverse=True)[:limit]

print(most_spoken_languages(filename="./data/countries_data.json", limit=3))


#3
def most_populated_countries(filename, limit):
    with open(filename) as f:
        countries=json.load(f)
        countries=sorted(countries, key=lambda country: country["population"], reverse=True)
        population=[{"country": country.get("name"), "population": country.get("population")} for country in countries[:limit]]
        return population
print(most_populated_countries(filename="./data/countries_data.json", limit=10))