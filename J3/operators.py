"""Jour 3 30 days of Python Programming"""
import math
age=25  #1
tall=1.70  #2
complex_number= 1+2j  #3
#4
base = int(input("Entrer la base: "))
height = int(input("Entrez la hauteur: "))
print("L'aire du triangle est: ", int(base)*int(height)*0.5)

#5
a = int(input("Entrez le côté a: "))
b = int(input("Entrez le côté b: "))
c = int(input("Entrez le côté c: "))
print("Le périmètre du triangle est: ", a+b+c)

#6
largeur = int(input("Entrer la largeur: "))
longueur = int(input("Entrer la longueur: "))
print("La surface du rectangle: ", largeur*longueur)
print("Le périmètre du rectange: ", 2*(largeur+longueur))

#7
circle_radius = int(input("Entrez le rayon: "))
print("L'aire du cercle: ", 3.14*(circle_radius**2))
print("La circonférence du cercle: ", 2*3.14*circle_radius)

#8 y = 2x -2
slope1=2
print("La pente est:", slope1)

#9
x=(2, 2)
y=(6, 10)
slope2=(y[1] - x[1])/(y[0] - x[0])
print("La pente est: ", slope2)
print("La distance euclidienne: ", math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2))

#10
print("Comparison slope1 is greater than slope2", slope1 > slope2)

#11
print("y = x^2 + 6x + 9  si x=2: ", 2**2 + 6*2 + 9)
print("y = x^2 + 6x + 9  si x=-1: ", -1**2 + 6*-1 + 9)
print("0 = x^2 + 6x + 9  si x=: ", -1**2 + 6*-1 + 9)
#il s'agit d'un carré parfait, 0=y=(x+3)² donc
print("x=", -3)

print(len('dragon') != len('python')) #12
print('on' in 'dragon' and 'on' in 'python')  #13
print('jargon' in 'I hope this course is not full of jargon')  #14
print('on' not in 'dragon' and 'on' not in 'python')  #15
print(float(len('python')), str(len('python')))  #16

#use modulo % operator (number % 2) #17
print((7//3) == int(2.7))  #18
print(type(10) == type('10'))
print(int(9.8) == 10)

#21
hours=int(input("Entrez le nombre d'heure: "))
rate = float(input("Entrez le taux horaire: "))
print("Votre revenu est ", hours*rate)

#22
years = int(input("Entrez l'age inferieur a 100: "))
years = min(years, 100)
print("Vous avez vécu: ", 60*60*24*365*years, " secondes")

#23
print(""""
        1 1 1 1 1
        2 1 2 4 8
        3 1 3 9 27
        4 1 4 16 64
        5 1 5 25 125
      """)
