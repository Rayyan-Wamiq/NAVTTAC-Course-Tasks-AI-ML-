import numpy as np

scores = np.array([78, 85, 92, 64, 89, 95, 71])

z_score = (scores - np.mean(scores)) / np.std(scores)

highest_z_index = np.argmax(z_score)
highest_score = scores[highest_z_index]

print("Highest Z-index:", highest_z_index)
print("Highest score:", highest_score)
