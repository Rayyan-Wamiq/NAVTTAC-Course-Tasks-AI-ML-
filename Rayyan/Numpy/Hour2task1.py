import numpy as np
n1 = np.arange(16)
print(n1)

z = n1.reshape(4,4)
print(z)

print(z[2,3])
print(z[3])
print(z[:,1])
print(z[0:2, 0:2])
print(z[-2:, -2:])