"""Day4 30 days of Python Programming"""

print('Thirty'+' '+'Days'+' '+'Of'+' '+'Python')  #1
print('Codinng'+' '+'For'+' '+'All')  #2
company="Coding For All"  #3
print(company)  #4
print("Length of the company string:", len(company))  #5
print("Upper case:", company.upper())  #6
print("Lower case:", company.lower())  #7

#8
company = "Coding For All"
print("Capitalize:", company.capitalize())
print("Title:", company.title())
print("Swap case:", company.swapcase())

#9
print("Cut out first word:", company[6:])
#10
print("Contains with in:", "Coding" in company)
print("Contains with find:", company.find("Coding"))
print("Contains with index:", company.index("Coding"))
#11
print(company.replace('Coding', 'Python'))
#12
print('Python for Everyone'.replace('Everyone', 'All'))
#13
print(company.split(' '))
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
#15
print("Char at index 0:", "Coding For All"[0])
#16
print("Latest char:", "Coding For All"[-1])
#17
print("Char at index 10:", "Coding For All"[10])
#18
literal="Python For Everyone"
literal=literal.split(" ")
accronyme=literal[0][0]+literal[1][0]+literal[2][0]
print("Acronyme of Python For Everyone:", accronyme)
#19
literal="Coding For All"
literal=literal.split(" ")
accronyme=literal[0][0]+literal[1][0]+literal[2][0]
print("Acronyme of Coding For All:", accronyme)
#20
print("Position of first occurence of C ", 'Coding For All'.index('C'))
#21
print("Position of first occurence of F ", 'Coding For All'.index('F'))
#22
print("Position of last occurence of l rfinf ", 'Coding For All'.rfind('l'))
#23
print("Position of first occurrence of because ", "'You cannot end a sentence with because because because is a conjunction".find("because"))
#24
print("Position of last occurrence of because ", "'You cannot end a sentence with because because because is a conjunction".rindex("because"))
#25
sentence = "You cannot end a sentence with because because because is a conjunction"
sentence = sentence[0:sentence.index("because")] + sentence[sentence.rindex("is"):]
print(sentence)
#26
print("Position of first occurrence of because ", "'You cannot end a sentence with because because because is a conjunction".index("because"))
#27
sentence = "You cannot end a sentence with because because because is a conjunction"
sentence = sentence[0:sentence.index("because")] + sentence[sentence.rindex("is"):]
print(sentence)
#28
print("Coding For All".startswith('Coding'))
#29
print("Coding For All".endswith('coding'))
#30
print("  Coding For All  ".strip())
#31
'''thirty_days_of_python return true when we use the method isidentifier'''

#32
print('# '.join(['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']))
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
#36
a=8
b=6
print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")
print("{} / {} = {:.2f}".format(a, b, a/b))
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
