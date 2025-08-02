"""Day7 30 days of Python Programming"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#1
print('it_companies length:', len(it_companies))
#2
it_companies.add('Twitter')
#3
it_companies.update(['Whatsapp', 'Instagram', 'Samsung', 'Acer'])
#'4
it_companies.pop()
#5
it_companies.remove('Twitter')
it_companies.discard('Yahoo') #Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.


#Exercises: Level 2
#1
C = A.union(B)
#2
I = A.intersection(B)
#3
print('Is A subset of B:', A.issubset(B))
#4
print('Are A and B disjoint sets:',A.isdisjoint(B))
#5
j_ab = A.union(B)
j_ba = B.union(A)
#6
print('Symmetric difference between A and B:', A.symmetric_difference(B))
#7
del A, B, C,I, j_ab, j_ba


#Exercises: Level 3
#1
age_st = set(age) #the length of the list is superior to the set
#2 The difference between the following data types: string, list, tuple and set
'''
 string and list are mutable, tuple are immutable. they use index to access element. with set, elements can't be duplicated, special method are applicable
 like mathematical operation such as union, symetric difference... Tuple have fewer methods than list and strings
'''
#3
sentence = "I am a teacher and I love to inspire and teach people"
print("Number of unique words:", len(set(sentence.split(" "))))