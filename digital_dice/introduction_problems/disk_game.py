# Digital Dice
# Problem 0.C

from random import uniform

p_11 = 0.2
p_12 = 0.4  # 0.2+0.4
p_21 = 0.3
p_22 = 0.35


wins = 0
pointer = 0
pointer2 = 0
for i in range(10**6):
    while pointer < p_11:
        pointer2 = 0  # resetting pointer2
        pointer = uniform(0, 1)
        if p_11+p_21 < pointer < 1:  # area corresponding to x_1
            wins += 1  # wins
            pointer = 0
            break
        else:
            pointer = 0  # resetting pointer1
            lost = False
            while pointer2 < p_22:
                pointer2 = uniform(0, 1)
                if p_22+p_21 < pointer2 < 1:  # area corresponding to x_2
                    pointer2 = 0
                    lost = True
                    break  # loses
            if lost:
                break

print(wins / 10**6)
print((1 - p_11 - p_12) * (1 - p_22) / ((1 - p_11) * (1 - p_22) - p_12 * p_21))
