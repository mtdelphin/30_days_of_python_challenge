"""Exercises: Level 1"""
#1
empty_list = list()
#2
items = list((1, 2, 3, 4, 5, 8, 9))
#3
print("Length:", len(items))
#4
print("First item: {}, middle: {}, last: {}".format(items[0], items[len(items)//2], items[-1]))
#5
mixed_data_types = ['Frank', 25, 1.70, 'single', 'cotonou']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print("Number of companies:", len(it_companies))
#9
print("First company: {}, middle: {}, last: {}".format(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]))
#10
it_companies[0]='Meta'
print(it_companies)
#11
it_companies.append('Apache')
#12
it_companies.insert(len(it_companies)//2, 'Apple')
#13
it_companies[-1]=it_companies[-1].upper()
#14
joined = '#; '.join(it_companies)
#15
print("Google exists ?", "Google" in it_companies)
#16
it_companies.sort()
#17
it_companies.reverse()
#18
first_3_companies = it_companies[0:3]
#19
last_3_companies = it_companies[-3:]
#20
middle_companie = it_companies[len(it_companies)//2]
#21
it_companies.pop(0)
#22
it_companies.remove(middle_companie)
#23
it_companies.pop(-1)
#24
it_companies.clear()
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end+back_end
#27
full_stack = joined.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')

print(full_stack)