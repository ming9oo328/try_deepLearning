import numpy as np

X = np.array([[51,55],[14,19],[0,4]])
X = X.flatten()
print(X)
print(X[np.array([0,2,4])])
print(X>15) #원소가 15초과인가?
print(X[X>15]) #원소 중 15가 넘는 원소만 출력