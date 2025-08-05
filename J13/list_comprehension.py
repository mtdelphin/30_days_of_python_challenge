"""Day13 30 days of Python Programming"""
#1
numbers=[-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero=[i for i in numbers if i<=0]

print(negative_zero)

#2
list_of_lists=[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [i for arr in list_of_lists for sub_arr in arr for i in sub_arr]

print(flatten)


#3
tpl=[(i, 1,)+tuple([i**j for j in range(2, 6)]) for i in range(11)]
print(tpl)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
ctr=[el for lst in countries for tpl in lst for el in [[tpl[0].upper(), tpl[0][:3].upper(), tpl[1].upper()]]]
print(ctr)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
ctr=[{"country": ct[0].upper(), "city": ct[1].upper()} for lst in countries for ct in lst]
print(ctr)

#6
names =  [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nms = [name[0]+' '+ name[1] for lst in names for name in lst]
print(nms)

#7
"""
Y intercept formula
y=mx+b
"""
y_intercept=lambda m, x, y:m*x*y
print("Y intercept of y=2x+9 where for x=3 is: ", y_intercept(2, 3, 9))