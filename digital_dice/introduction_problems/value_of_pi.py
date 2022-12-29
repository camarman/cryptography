from random import uniform

P = 0
N = 10 ** 6
for j in range(N):
    x_1 = uniform(0, 1)
    y_1 = uniform(0, 1)
    if x_1**2 + y_1**2 < 1:
        P += 1
pi = 4 * P / N
print("pi=", pi)
