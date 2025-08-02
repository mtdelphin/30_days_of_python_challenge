"""Day11 30 days of Python Programming"""
###Exercices: Level 1
#1
def evens_and_odds(nb: int):
    evens = odds = 0

    for n in range(nb+1):
        if n%2!=0 :
            odds += 1
        else:
            evens += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))


#2
def factorial(nb):
    res = 1
    for i in range(nb, 0, -1):
        res *= i
    print(f"Factorial of {nb} is {res}")

factorial(0)
factorial(3)

#3
def is_empty(arg):
    if len(arg) == 0:
        return True
    return False

print("is empty :", is_empty(""))
print("[] is empty :", is_empty([]))
print("[1] is empty :", is_empty([1]))
print("iueuire is empty :", is_empty("iueuire"))

#4

def calculate_mean(lst: list):
    if is_empty(lst):
        return "List is empty to calculate the mean"
    
    return sum(lst)/len(lst)

print("The mean is", calculate_mean([]))
print("The mean is", calculate_mean([2 , 4 , 6 , 8]))

def calculate_median(lst: list):
    if is_empty(lst):
        return "List is empty to calculate the median"
    lst = sorted(lst)
    if len(lst)%2 == 0:
        return (lst[int(len(lst)/2) - 1] + lst[int(len(lst)/2) +1])/2
    else:
        return (lst[(len(lst)//2)])
    
print("The median is", calculate_median([]))
print("The median is", calculate_median([2 , 4 , 6 , 8]))
print("The median is", calculate_median([1, 2 , 4 , 6 , 8]))


def calculate_mode(lst: list):
    lst_uniq = set(lst)
    mode = None
    frequence = 0
    for item in lst_uniq:
        if lst.count(item) > frequence:
            frequence = lst.count(item)
            mode=item

    return mode

print("The mode is", calculate_mode([]))
print("The mode is", calculate_mode([1, 2, 3, 3, 4, 3 , 4 , 6 , 8]))


def calculate_range(lst: list):
    if is_empty(lst):
        return "List is empty to calculate the range"
    return max(lst) - min(lst)

print("The range is ", calculate_range({}))
print("The range is ", calculate_range({8, 3, 7, 1, 3, 9}))

def calculate_variance(lst: list):
    mean = calculate_mean(lst)
    diff_from_means=[i-mean for i in lst]
    squarred_diff = [i**2 for i in diff_from_means]
    sum_squarred_diff = sum(squarred_diff)
    return sum_squarred_diff/len(lst)

print("The variance is ", calculate_variance([1, 2, 3, 4, 5]))

import math
def calculate_std(lst: list):
    variance = calculate_variance(lst)
    return math.sqrt(variance)

print("The standard deviation is ", calculate_std([10, 12, 23, 23, 16, 23, 21, 16]))
