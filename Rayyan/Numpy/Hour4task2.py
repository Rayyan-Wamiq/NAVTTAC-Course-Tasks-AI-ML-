import numpy as np
arr  = np.array([54, 60, 44, 66, 23, 51, 79, 45])
print(np.sum(arr))

print(np.mean(arr))

print(np.max(arr))

print(np.min(arr))

print(np.std(arr))



arr2 = np.array([[32, 45, 56, 33], [33, 44, 55, 66]])
print(np.sum(arr2, axis=0))  
print(np.sum(arr2, axis=1))
