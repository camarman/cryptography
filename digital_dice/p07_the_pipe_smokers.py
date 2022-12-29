# Digital Dice
# Problem 7: The Pipe Smoker’s Discovery

from random import uniform


step_size = 10**6
avg_drown_match = 0
for i in range(step_size):
    box_1, box_2 = 40, 40
    drown_match = 0
    while box_1 > 0 and box_2 > 0:
        box_random = uniform(0, 1)
        if box_random > 0.5:
            box_1 += -1
            drown_match += 1
        else:
            box_2 += -1
            drown_match += 1
    avg_drown_match += drown_match
print(avg_drown_match / step_size)
