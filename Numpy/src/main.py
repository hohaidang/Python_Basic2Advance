'''
Created on Dec 7, 2019

@author: prnsoft
'''

import numpy as np

# a = np.array([1, 2, 5])
# print(type(a))
# print(a)
# print(a.shape)
# print(a[0], a[1], a[2])
# 
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)
# print(b)

# --------------LOOP all elements in 2 Dimentional array --------------
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# b = np.zeros([100, 100, 3])
# rows = a.shape[0]
# cols = a.shape[1]
# for x in range(0, rows):
#     for y in range(0, cols):
#         print(a[x,y])
# ----------------------------------------------------------------------

# b = a[:2, 1:3]
# print(b)
# print(a[0, 1])
# b[0, 0] = 77
# print(a[0, 1])
# row_r1 = a[1, :]
# row_r2 = a[1:2, :]
# print(row_r1, row_r1.shape)
# print(row_r2, row_r2.shape)
# 
# col_r1 = a[:, 1]
# col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape)
# print(col_r2, col_r2.shape)

# a = np.array([[1, 2], [3,4], [5,6]])
# print(a)
# print(a[[0, 1, 2], [0, 1, 0]]) # Se lay vi tri a[0,0] a[1,1] a[2,0]
# print(a[[0,0], [1, 1]]) # Se lay vi tri a[0,1] va a[0,1]
# 
# a = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [10,11,12]])
# print(a)
# b = np.array([0, 2, 0, 1])
# print(b)
# c = np.arange(4)
# print(c)
# print(a[c, b])


# a = np.array([[1,2], [3,4], [5,6]])
# bool_idx = (a == 2)
# print(bool_idx)
# 
# print(a[bool_idx])
# print(a[a > 2])

# a = [0,1,2,3,4]
# b = a[::-2] # Tu so -1 nhay coc moi lan 2 don vi
# # vi tri -1 = 4, nhay len -3 la 2 va -5 la 0
# print("a = ", a)
# print("b = ", b)
# 
# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)
# print("Type Zip = ", type(zipped))
# print("List Zip = ", list(zipped))


# i, j = np.indices((2,3)).reshape(2  , -10)
# M = 2*i
# print(i)
# print(j)

# x = np.arange(20).reshape(20, -1)
# print(x)

coords = np.indices((2, 3)).reshape(2, -1)

if __name__ == '__main__':
    pass