# Digital Dice
# Problem 0.A

import numpy as np


total_correct = 0
for j in range(10**6):
    random_perm = np.random.permutation([i for i in range(5)])
    correct = 0
    for i in range(5):
        if random_perm[i] == i:
            correct += 1
    total_correct += correct
print(total_correct / 10**6)
