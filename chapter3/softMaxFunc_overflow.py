import numpy as np

a = np.array([1010,1000,990])
print(np.exp(a) / np.sum(np.exp(a))) #오버플로우 발생

c = np.max(a)
print(np.exp(a-c)/np.sum(np.exp(a-c)))


