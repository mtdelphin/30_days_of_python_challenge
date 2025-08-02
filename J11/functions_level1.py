"""Day11 30 days of Python Programming"""
###Exercices: Level 1
#1
def add_two_numbers(a, b):
    return a+b
print("Sum of 3 and 9 is:", add_two_numbers(3, 9))
#2
def area_of_circle(rad):
    return f"Area of circle with {rad} radius is: {3.14*(rad**2)}"

print(area_of_circle(4))

#3
def add_all_nums(*args):
    sum = 0
    for i in args:
        if (type(i)!=int and type(i)!=float):
            return "All inputs must be numbers"
        sum += i
    return sum
print("The sum of all number is:", add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, 3, 4, 5, "string"))

#4
def convert_celsius_to_fahrenheit(deg):
    return "Temperature {}° = {:.2f}".format(deg, (deg*9/2)+32)
print(convert_celsius_to_fahrenheit(23))

#5
def check_season(month: str):
    seasons = {"Autumn": ["September", "October" "November,"],
          "Winter": ["December", "January", "February"], 
          "Spring": ["March", "April", "May"],
          "Summer": ["June", "July", "August"]
        }
    for season in seasons:
        if month.capitalize() in seasons.get(season):
            return f"Season of month {month} is {season}"
        
    return f"Season not found for month {month}"
    
print(check_season("may"))
#6

def calculate_slope(x:tuple, y:tuple):
    """
    From two points (x₁, y₁) and (x₂, y₂)
    The slope m = (y₂ - y₁) / (x₂ - x₁)
    """
    return "The slope from points {} and {} is {:.2f}".format(x, y, (y[1] - x[1])/(y[0] - x[0]))


print(calculate_slope((1, 3), (3, 6)))


#7
import math
def solve_quadratic_eqn(a, b, c):
    """
    Equation have the structure: ax2 + bx + c = 0
    Δ=b²-4ac

    If Δ > 0 : two real distinct solutions
    x1=(-b - vΔ)/2a, x2=(-b + vΔ)/2a

    If Δ = 0 : One real solution (double)
    x=(-b)/2a

    If Δ < 0 : No real solution  (but two complex solutions)
    x1=(-b - jv|Δ|)/2a, x2=(-b + jv|Δ|)/2a
    """

    discr = b**2 - 4*a*c
    if discr == 0:
        print(f"The equation have one double real solution: {(-1*b)/2*a}")
    elif discr > 0:
        print("The equation have two real solutions ", end=" ")
        print("x1=",((-1*b)-math.sqrt(discr))/(2*a), "x2=", ((-1*b)+math.sqrt(discr))/(2*a))
    else:
        print("The equation have two complex solutions ", end=" ")
        print("x1=",((-1*b)-(math.sqrt(abs(discr))*1j))/(2*a), "x2=",((-1*b)+(math.sqrt(abs(discr))*1j))/(2*a))

solve_quadratic_eqn(1, -6, 9)
solve_quadratic_eqn(2, -4, -6)
solve_quadratic_eqn(1, 4, 13)

#8
def print_list(lst: list):
    print("Element of the list are: ", end="")
    for i in lst:
        print(i, end="" if i== lst[-1] else ", ")
    print()

print_list([1, 3, 4, 9])

#9
def reverse_list(lst: list):
    rvlst = []

    for i in lst[::-1]:
        rvlst.append(i)

    print("Reversed is:", rvlst)

reverse_list(["A", "B", "C", "D", "E"])

def capitalize_list_items(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    print("Capitalized list is:", lst)

capitalize_list_items(["cotonou", "lome", "abidjan", "lagos"])

#11
def add_item(lst: list, arg):
    lst.append(arg)
    print("Final list is:", lst)

add_item(["One", "Two", "Three"], "Four")

#12
def remove_item(lst: list, arg):
    lst.remove(arg)
    print("Final list is:", lst)

remove_item(["One", "Two", "Three", "Four", "Five"], "Four")

#13
def sum_of_number(nb):
    sum=0
    for n in range(nb+1):
        sum += n
    print(f"Sum of number to {nb} is {sum}")

sum_of_number(5)
sum_of_number(10)
sum_of_number(100)

#14
def sum_of_odds(nb):
    sum=0
    for n in range(nb+1):
        if n%2==0 :
            sum += n 
    print(f"Sum of odds to {nb} is {sum}")
sum_of_odds(10)

#15
def sum_of_evens(nb):
    sum=0
    for n in range(nb+1):
        if n%2!=0 :
            sum += n 
    print(f"Sum of evens to {nb} is {sum}")

sum_of_evens(10)

