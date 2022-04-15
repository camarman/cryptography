# Digital Dice
# Problem 0.A

from itertools import permutations
import numpy as np

totalcorrect = 0
for j in range(10**6):
    random_perm = np.random.permutation([i for i in range(5)])
    correct = 0
    for i in range(5):
        if random_perm[i] == i:
            correct += 1
    totalcorrect += correct
print(totalcorrect / 10**6)
