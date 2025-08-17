import requests
import re
import statistics
from bs4 import  BeautifulSoup
from functools import reduce
from collections import Counter

#1
url='https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response=requests.get(url)

txt = response.text
words=Counter(txt.split())
print(words.most_common(10))


#2
url='https://api.thecatapi.com/v1/breeds'
try:
    #i
    cats=requests.get(url).json()
    lst=[[int(elm) for elm in re.findall(r'\d+', cat.get('weight').get('metric'))] for cat in cats]
    weights=reduce(lambda arr, item: arr+item, lst)
    
    print('Min: ', min(weights))
    print('Max: ', max(weights))
    print('Median: ', statistics.median(weights))
    print('Mean: ', statistics.mean(weights))
    print('Stantard deviation: ', statistics.stdev(weights))

    #ii
    lst=[[int(elm) for elm in re.findall(r'\d+', cat.get('life_span'))] for cat in cats]
    lifespan=reduce(lambda arr, item: arr+item, lst)
    
    print('Min: ', min(lifespan))
    print('Max: ', max(lifespan))
    print('Median: ', statistics.median(lifespan))
    print('Mean: ', statistics.mean(lifespan))
    print('Stantard deviation: ', statistics.stdev(lifespan))

    #iii
    breed_country=Counter([cat.get('origin') for cat in cats])
    print(breed_country)

except Exception as e:
    print('An error occurs: ', e)


#3
url='https://countries-api-abhishek.vercel.app/countries'
try:
    countries=requests.get(url).json().get('data')

    #i
    ten_largest=sorted(countries, key=lambda ctr: ctr.get('area'), reverse=True)[:10]
    print('Ten largest countries:')
    print(ten_largest)
    #2
    langages=reduce(lambda lang, items: lang+items, [ctr.get('languages') for ctr in countries])
    ten_most_spoken_lan=Counter(langages).most_common(10)
    print('Ten most spoken langages:')
    print(ten_most_spoken_lan)
    #3
    nbr_language=len(set(langages))
    print('Number total of languages:', nbr_language)
except Exception as e:
    print(e)


#4
url='https://archive.ics.uci.edu/datasets'
try:
    response=requests.get(url).text
    html=BeautifulSoup(response, 'html.parser')
    print(html.prettify())
except Exception as e:
    print(e)
