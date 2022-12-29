# Digital Dice
# Problem 9: The Forgetful Burglar Problem

from random import uniform


def next_town():
    """
    Calculating the step to the next town by using random.uniform

    Returns:
        [int]: the next movement of the burglar
    """
    step_num = uniform(0, 1)
    if 0 <= step_num < 0.25:
        return 2
    elif 0.25 <= step_num < 0.50:
        return 1
    elif 0.50 <= step_num < 0.75:
        return -1
    else:
        return -2


k = 5

step_size = 10**6
prob = 0
for step in range(step_size):
    burglar_visited_house = [0]
    current_house = 0
    for i in range(1, 10):
        current_house += next_town()
        if current_house in burglar_visited_house and i == k:
            prob += 1
            break
        elif current_house in burglar_visited_house and i != k:
            break
        else:
            burglar_visited_house.append(current_house)

print(prob / step_size)
