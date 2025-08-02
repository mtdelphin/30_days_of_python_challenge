"""Day10 30 days of Python Programming"""

#Exercices: Level 1
#1
for i in range(0, 10):
    print(i)

print("--------------")

i=0
while i < 10:
    print(i)
    i += 1

#2
print("--------------")

i=10
#1
for i in range(10, 0, -1):
    print(i)

print("--------------")

i=10
while i > 0:
    print(i)
    i -= 1

#3
for i in range(7):
    print("#" * i)

#4
for i in range(8):
    for j in range(9):
        print(" #", end=" ")
    print()

#5
for i in range(11):
    print(f"{i} x {i} = {i*i}")

#6
for it in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(it)

for i in range(0, 100, 2):
    print(i)

for i in range(100):
    if i % 2 !=2:
        print(i)


#Exercice 2
sumbr = 0
for i in range(101):
    sumbr += i

print(f"The sum of all number is {sumbr}")


sumev = sumod = 0
for i in range(101):

    if i%2 == 0:
        sumev += i
    else:
         sumod += i

print(f"The sum of all evens number is {sumev}. And the sum of all odds is {sumod}")


#Exercices:Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

countries_and = []
for country in countries:
    if "land" in country:
        countries_and.append(country)

print("Countries with the word 'land':", countries_and)

#2
fruits = ['banana', 'orange', 'mango', 'lemon']
fruitsrv=[]
for index in range(len(fruits)-1, -1, -1):
    fruitsrv.append(fruits[index])

print("Reversed fruits: ", fruitsrv)

#3 i
from country_data import get_country_data

countries_data = get_country_data()

langages = []
for country in countries_data:
    langages += country.get("languages")

print("Total number langage:", len(set(langages)))

#3 ii
apparition = {}
for langage in langages:
    if not langage in apparition:
        apparition[langage] = langages.count(langage)

apparition_sorted = dict(sorted(apparition.items(), key= lambda item: item[1], reverse=True))
print("The most ten spoken langage : ", list(apparition_sorted.keys())[:10])


#3 iii
country_sorted_by_population = sorted(countries_data, key= lambda country:country["population"], reverse=True)
populated = []
for ctr in country_sorted_by_population:
    populated.append(ctr["name"])
    if(len(populated) == 10):
        break

print("Ten most populated countries: ", populated)
