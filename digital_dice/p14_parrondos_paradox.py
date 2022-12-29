# Digital Dice
# Problem 14: Parrondo’s Paradox

from random import uniform
from matplotlib import pyplot as plt
from numpy import array, zeros


def gameA(capital, probH=1/2, eps=0.005):
    """
    Calculating the result of a coin toss, given that the probability of a head and the epsilon(e)

    Args:
        capital [int]: The money of the gambler
        probH [float, optional]: The probability of obtaining head from a biased coin. The value must be between (0-1). Defaults to 1/2.
        eps [float, optional]: the deviation from the biased coin probability. Defaults to 0.005.

    Returns:
        capital [int]: The money of the gambler after the coin toss
    """
    if uniform(0, 1) < probH - eps:
        capital += 1
    else:
        capital -= 1
    return capital


def gameB(capital, coin1_probH=1/10, coin2_probH=3/4, eps=0.005):
    """
    Calculating the result of a coin toss, given that the probability of a head and the epsilon(e)

    Args:
        capital [int]: The money of the gambler
        coin1_probH [float, optional]: The probability of obtaining head from a biased coin 1. The value must be between (0-1). Defaults to 1/10.
        coin2_probH [float, optional]: The probability of obtaining head from a biased coin 2. The value must be between (0-1). Defaults to 3/4.
        eps [float, optional]: the deviation from the biased coin probability. Defaults to 0.005.

    Returns:
        capital [int]: The money of the gambler after the coin toss
    """
    if capital % 3 == 0:
        if uniform(0, 1) < coin1_probH - eps:
            capital += 1
        else:
            capital -= 1
    else:
        if uniform(0, 1) < coin2_probH - eps:
            capital += 1
        else:
            capital -= 1
    return capital


def play_game1():
    """
    Computing 100 single games for part 1

    Returns:
        The progress of the capital per time (coin_flip)
    """
    Mj = []
    capital = 0
    for k in range(1, 101):
        capital_updated = gameB(capital)
        Mj.append(capital_updated)
        capital = capital_updated
    return array(Mj)


def play_game2():
    """
    Computing 100 single games for part 2

    Returns:
        The progress of the capital per time (coin_flip)
    """
    Mj = []
    capital = 0
    for k in range(1, 101):
        if uniform(0, 1) > 0.5:
            capital_updated = gameB(capital)
        else:
            capital_updated = gameA(capital)
        Mj.append(capital_updated)
        capital = capital_updated
    return array(Mj)


step_size = 10**5
k_values = [i for i in range(1, 101)]

#### Part A####

# Mk1 = zeros(100)
# for sequence in range(step_size):
#     Mk1 += play_game1() / step_size


# plt.plot(k_values, Mk1, label='$\\varepsilon = 0.005$')
# plt.xlabel('Number of coin flips')
# plt.ylabel('Ensemble average of capital')
# plt.title('Game B')
# plt.legend()
# plt.show()


#### Part B ####

Mk2 = zeros(100)
for sequence in range(step_size):
    Mk2 += play_game2() / step_size


plt.plot(k_values, Mk2, label='$\\varepsilon = 0.005$')
plt.xlabel('Number of coin flips')
plt.ylabel('Ensemble average of capital')
plt.title('Game A and Game B chosen randomly over time')
plt.legend()
plt.show()
