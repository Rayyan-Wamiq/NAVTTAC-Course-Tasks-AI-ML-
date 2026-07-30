import numpy as np
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.savetxt("data.csv",arr,delimiter=",")

loaded = np.loadtxt("data.csv",delimiter=",")
print(loaded)
