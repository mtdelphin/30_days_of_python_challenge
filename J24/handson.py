import numpy as np

python_list = [1,2,3,4,5]
# print(python_list)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
#print(two_dimensional_list)

np_array_from_list=np.array(python_list, dtype=float)
# print(np_array_from_list)

# print(np.array([0, 1, -1, 0, 0], dtype=bool))
np_array_two_dim=np.array(two_dimensional_list)

# print(type(np_array_two_dim))

# print(np_array_two_dim.shape)
# print(np_array_from_list.dtype)
# print(np_array_two_dim / 2)

#-----------------getting items
# print(np_array_two_dim[0], np_array_two_dim[1:,2])
print(np_array_two_dim)
print(np_array_two_dim[::])
print(np_array_two_dim[::-1, ::-1])
np_array_two_dim[1, 2]=33
print(np_array_two_dim)

numpy_ones = np.ones((2,3),dtype=int,order='C')
print(numpy_ones)
numpy_ones=numpy_ones.reshape(3, 2)
print(numpy_ones)
flattened = numpy_ones.flatten()
print(flattened)
arr1, arr2=np.array([1, 2, 3]), np.array([4, 5, 6])

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))


print(np.random.random_integers(1, 9, size=(3, 4)))