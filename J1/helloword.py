#  distance eclidienne entre (2, 3) et (10, 8)
#  revient mathematiquement a racine carré de (a1-b1) au carré + (a2-b2)au carré selon wiki
import math
a=(2,3)
b=(10,8)
distance = math.isqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
print("distance entre  (2, 3) et (10, 8) : ")
print(distance)
