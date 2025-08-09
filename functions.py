def sum_number(num):
    return sum(num)


print(sum_number([1, 2, 3, 4, 5]))

def call(method, param):
    r = method(param)
    return r
def concat(country):
    return f"The country {country}"+" is on the earth."

print(call(concat, "Togo"))

def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if(x>0):
        return x
    return -x


def high_order_function(type):
    if type=='square':
        return square
    elif type=='cube':
        return cube
    elif type=='absolute':
        return absolute
    
function = high_order_function('cube')
print(function(16))


def add_ten():
    ten=10
    def add(n):
        return n+ten
    return add

val=add_ten()
print(val(6))



#decorators
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g=uppercase_decorator(greeting)


print(g())


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_str = func.split()
        print(splitted_str)
        return splitted_str
    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python Z"

print(greeting())

