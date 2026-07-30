import numpy as np
temp = np.array([10, 40, 15, 32, 55, 9])
mask = temp >= 25
print(mask)

passing = temp[mask]
print(passing)

temp[temp < 0] = 0   
print(temp)

    