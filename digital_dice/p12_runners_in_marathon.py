# Digital Dice
# Problem 12: How Many Runners in a Marathon?

from random import randint
from matplotlib import pyplot as plt


def true_sample_error(n_percentage):
    N = randint(100, 1000)
    n = int((N * n_percentage) / 100)
    random_values = [randint(1, N) for i in range(n)]
    E_max = max(random_values)
    N_estimated = (n + 1) * (E_max / n) - 1
    error = (100 * (N_estimated - N)) / N
    return error

error_values = []
for i in range(10**4):
    error_values.append(true_sample_error(20))

plt.hist(error_values, bins = 100)
plt.xlabel('Percent error')
plt.ylabel('Number of simulations')
plt.show()
