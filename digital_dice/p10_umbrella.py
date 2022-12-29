# Digital Dice
# Problem 10: The Umbrella Quandary

from random import uniform
from matplotlib import pyplot as plt
from numpy import arange


step_size = 10**4


def is_rain(p):
    """
    Determines if it's going to rain or not for a given probability

    Args:
        p [float]: the probability of raining. Take values between 0 and 1

    Returns:
        True, if its going to rain and false if it's not going to rain
    """
    prob_rain = uniform(0, 1)
    if prob_rain > p:
        return False
    else:
        return True


def next_loc(current_position):
    """
    An iterator to calculate the next position of the person between home and office

    Args:
        current_position [string]: Current position of the person

    Returns:
        [string]: The next location of the person
    """
    if current_position == 'home':
        return 'office'
    else:
        return 'home'


def prob_wet_calc(p, home_umbrella_num, office_umbrella_num):
    """
    Calculating the average time before the first soaking for a given probability of rain and
    the umbrella numbers for the both locations

    Args:
        p [float]: the probability of raining. Takes values between 0 and 1
        home_umbrella_num [int]: The number of umbrellas at the home 
        office_umbrella_num [int]: The number of umbrellas at the office

    Returns:
        the average time of getting wet
    """
    time = 0
    current_position = 'home'
    wet = False
    while not wet:
        if is_rain(p):
            if current_position == 'home' and home_umbrella_num != 0:
                home_umbrella_num -= 1
                office_umbrella_num += 1
                current_position = 'office'
                time += 1
            elif current_position == 'office' and office_umbrella_num != 0:
                home_umbrella_num += 1
                office_umbrella_num -= 1
                current_position = 'home'
                time += 1
            else:
                wet = True
        else:
            current_position = next_loc(current_position)
            time += 1
    return time


p_values = arange(0.01, 1, 10**(-2)) # taking different p values
avg_time_values = []
for p in p_values:
    avg_time = 0
    for i in range(step_size):
        time = prob_wet_calc(p, 2, 2) # In this case we have (1, 1) umbrella
        avg_time += time
    avg_time_values.append(avg_time / step_size)

plt.plot(p_values, avg_time_values)
plt.xlabel('Probability of rain')
plt.ylabel('Average number of walks before first soaking')
plt.grid(True)
plt.show()
