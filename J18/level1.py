"""Day18 30 days of Python Programming"""

import re

#1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words=re.findall(r'\w+', paragraph)

uniwords=set(words)
counts=map(lambda w: words.count(w), uniwords)

appearance=[(c, w) for w, c in zip(uniwords, counts)]

appearance=sorted(appearance, key=lambda st: st[0], reverse=True)
print(f"The most frequent word is \"{appearance[0][1]}\"")


#2
txt='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

pattern=r"-?\d+"
numbers=re.findall(pattern, txt)
numbers=sorted([int(n) for n in numbers])
distance=numbers[-1] - numbers[0]
print("The distance between the two furthest particles is ", distance)