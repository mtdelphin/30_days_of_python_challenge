"""Day14 30 days of Python Programming"""
import functools
#1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Level1
#1
"""
Difference entre map, filter, et reduce.

`map` renvoie un nouvel objet itérable en appliquant une fonction à chaque élément d'une séquence.  
`filter` renvoie un nouvel objet itérable contenant uniquement les éléments qui respectent un certain critère défini dans une fonction.  
`reduce`, qui appartient à un module externe à importer, combine tous les éléments en un seul résultat au lieu de renvoyer un objet itérable.

"""

#2
"""
Difference entre higher order function, closure and decorator
Une higher-order function est une fonction qui peut recevoir une autre fonction en paramètre ou retourner une fonction.  
Une closure est une fonction définie à l’intérieur d’une autre, qui peut utiliser les variables de la fonction extérieure, même après son exécution.  
Un décorateur est une forme particulière de closure utilisée pour modifier le comportement d’une fonction. Le symbole @ permet de l’appliquer automatiquement à une fonction cible. Une fonction peut avoir plusieurs décorateurs.
"""

#3
def call_cube(x):
    return x**3

def call_odd(x):
    return x%2==0

def call_id(x, y):
    return x+y


numbers_cube=map(call_cube, numbers)
print(list(numbers_cube))
print(list(filter(call_odd, numbers)))
print(functools.reduce(call_id, numbers))

#4
for ctr in countries:
    print(ctr)

for nm in names:
    print(nm)

for nbr in numbers:
    print(nbr)