# Digital Dice
# Problem 1: The Clumsy Dishwasher Problem

from random import uniform


step_size = 10**6
clumsy = 0
for i in range(step_size):
    broken_dish = [uniform(0, 1) for i in range(5) if uniform(0, 1) < 0.2]
    if len(broken_dish) >= 4:
        clumsy += 1
print(clumsy / step_size)
