import numpy as np
arr = np.array([[43,33,23,63], [34,56,22,54]])

z = np.sum(arr, axis=0)
z2 = np.sum(arr, axis=1)

print(" ",z)
print(" ",z2)


z3 = np.max(arr)
print(z3)

