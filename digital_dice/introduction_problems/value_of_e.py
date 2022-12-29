from random import uniform

# L is the length of the sequence, for [0.3, 0.4, 0.12] L = 3

sum = 0
for i in range(10 ** 6):
    L = 1
    x_1 = uniform(0, 1)
    while True:
        x_2 = uniform(0, 1)
        if x_2 > x_1:
            L += 1
            x_1 = x_2
        else:
            L += 1
            break
    sum += L
print('e=', sum / 10**6)  # this is equal to e
