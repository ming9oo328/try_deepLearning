import numpy as np

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])

C = np.dot(A,B)
D = np.dot(B,A)
print(C)
print(C.shape)
print(D)
print(D.shape)