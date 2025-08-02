"""Day9 30 days of Python Programming"""
###Exercices: Level 1
#1
age=int(input("Entrez votre age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18-age} more years to learn to drive.")

#2
my_age = 25
diff=abs(age - my_age)

print(f"I'am {my_age}")
if age == my_age:
    print("You and I have the same age")
elif age < my_age:
    print("I'm 1 year older than you") if diff== 1 else print(f"I'm {diff} years older than you.")
else:
    print("Your are 1 year older than me") if diff== 1 else print(f"You are {diff} years older than me.")

#3
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


###Exercices: Level 2
#1

score = int(input("Enter your score: "))
if 0<=score<=49:
    print("Your grade is F")
elif 50<=score<=59:
    print("Your grade is D")
elif 60<=score<=69:
    print("Your grade is C")
elif 70<=score<=79:
    print("Your grade is B")
elif 80<=score<=100:
    print("Your grade is A")
else:
    print(f"Your score should be between 0 and 100! Are you an extra terrestre?? Mister/Mrs {score} scored")

#2
seasons = {"Autumn": ["September", "October" "November,"],
          "Winter": ["December", "January", "February"], 
          "Spring": ["March", "April", "May"],
          "Summer": ["June", "July", "August"]}
month = input("Enter the month: ")
if month in seasons.get("Autumn"):
    print("The season is Autumn")
elif month in seasons.get("Winter"):
    print("The season is Winter")
elif month in seasons.get("Spring"):
    print("The season is Spring")
elif month in seasons.get("Summer"):
    print("The season is Summer")
else:
    print(f"The season is not not known for the month {month}")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if not fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')


###Exercices: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person.keys():
    print(person["skills"][(len(person["skills"])//2) - 1])
    if "Python" in person["skills"]:
        print("Person has 'Python' skill")
    if "Javascript" in person['skills'] and  "React" in person['skills'] and 2==len(person['skills']):
        print("He is a frontend developer")
    elif "Node" in person['skills'] and  "Python" in person['skills'] and  "Mongo" in person['skills'] and 3==len(person['skills']):
        print("He is a backend developer")
    elif "React" in person['skills'] and  "Node" in person['skills'] and  "Mongo" in person['skills']:
        print("He is a fullstack developer")

info = person.get("first_name") + " " + person.get("last_name") + f" lives in {person.get("country")}. He is"
info += " married." if person.get("is_married") else " not married."
print(info)