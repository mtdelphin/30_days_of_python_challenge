import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


normal_array = np.random.normal(79, 15, 80)
sns.set()

print(plt.hist(normal_array, color="grey", bins=50))
plt.show()


print("linspace")
print(np.linspace(1.0, 5.0, num=10))

np_normal_dis = np.random.normal(5, 0.5, 100)

## min, max, mean, median, sd
two_dimension_array=np.array([(1,2,3), (4,5,6)])
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
#print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


a = [1,2,3]
print('Tile:', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))

