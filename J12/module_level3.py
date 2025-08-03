"""Day12 30 days of Python Programming"""
import random

#Exercices: Level3
#1
def shuffle_list(lst: list):
    finalst=[]
    while len(lst) !=0:
        index = random.randint(0, len(lst)-1)
        finalst.append(lst[index])
        del lst[index]

    return finalst


print(shuffle_list([1, 2, 3, 4, 5]))

#2
def rand_7_uniq_num():
    numbers=set()
    while len(numbers) != 7:
        numbers.add(random.randint(0, 9))
    
    return numbers
print(rand_7_uniq_num())