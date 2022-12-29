# Digital Dice
# Problem 0.B

import numpy as np
from random import randint


total_correct = 0
for j in range(10**5):
    random_perm = np.random.permutation([i for i in range(24)])
    correct = 0
    for i in range(24):
        random_num = randint(0, 23)
        if random_perm[i] == random_num:
            correct += 1
    total_correct += correct
print(total_correct / 10**5)
