# Will you be alive in 10 years from now ?
# BProblem 1: Breaking Sticks part a

from random import randint, uniform
from numpy import linspace


def split_tester(pos_mark1, pos_mark2, n):
    """
    Function that tests whetever two marks are on the same piece of the broken stick

    param [int] n: breaking the stick into n equal length pieces
    returns [boolean]: True, if the two marks are on the same piece on the broken stick
    """
    pieces = sorted([0, *[uniform(0, 1) for i in range(n-1)], 1])
    for i in range(len(pieces) - 1):
        if pieces[i] <= pos_mark1 <= pieces[i+1]:
            if pieces[i] <= pos_mark2 <= pieces[i+1]:
                return True
            else:
                return False


n = 7
counter = 0
for i in range(10**6):
    pos_mark1 = uniform(0, 1.000000001)  # so that 1 could be included.
    pos_mark2 = uniform(0, 1.000000001)  # so that 1 could be included.
    if split_tester(pos_mark1, pos_mark2, n):
        counter += 1
print("The theortical probsability:", round(2/(n+1), 6))
print("Computational result: ", round(counter/10**6, 6))
