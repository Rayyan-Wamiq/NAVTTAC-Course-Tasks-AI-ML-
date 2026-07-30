import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
np.save("random_data.npy",arr)

loaded = np.load("random_data.npy")
print(loaded)