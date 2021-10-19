# Digital Dice
# Problem 0.B

from itertools import permutations
import numpy as np
from random import randint


totalcorrect = 0
for j in range(10**5):
    random_perm = np.random.permutation([i for i in range(24)])
    correct = 0
    for i in range(24):
        random_num = randint(0, 23)
        if random_perm[i] == random_num:
            correct += 1
    totalcorrect += correct
print(totalcorrect / 10**5)
