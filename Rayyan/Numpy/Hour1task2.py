import numpy as np
exam_score = np.array([78,89,77,83,65])
student_ages = np.array([21,22,19,20,23])
np.savez("Student_data.npz",first=exam_score, second=student_ages)

data = np.load("student_data.npz")
print(data["first"])
print(data["second"])

