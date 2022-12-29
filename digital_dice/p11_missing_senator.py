# Digital Dice
# Problem 11: The Case of the Missing Senators

from random import uniform


def is_bill(against_senator, missing_senator):
    for_senator = 100 - against_senator
    for i in range(missing_senator):
        if uniform(0, 1) >= 0.5:
            against_senator -= 1
        else:
            for_senator -= 1
    if against_senator > for_senator:
        return True  # the against senators defeat the bill


against_senator = int(input("Enter the against the bill senators, A: "))
missing_senator = int(input("Enter the missing senator number, M: "))

step_size = 10**6

total_win = 0
for i in range(step_size):
    if is_bill(against_senator, missing_senator):
        total_win += 1

print(total_win / step_size)


