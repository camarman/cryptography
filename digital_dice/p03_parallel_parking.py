# Digital Dice
# Problem 3: A Parallel Parking Question

from random import choice, uniform


def mutual_pair_finder(L):
    """
    Finding the points in a list where they are a member of mutual neighbours

    Args:
        L [list]: A list containing random number

    Returns:
        [set]: Members of the mutual neighbours points
    """
    mutual_pairs = []
    # first calculating the nearest neighbours of each point and storing them in a list
    nearest_ngbh = [[L[0], L[1]], [L[n-1], L[n-2]]]
    for i in range(1, n-1):
        if L[i+1] - L[i] > L[i] - L[i-1]:
            nearest_ngbh.append([L[i], L[i-1]])
        else:
            nearest_ngbh.append([L[i], L[i+1]])
    # from now on we can calculate the points in L that is a member of mutual neighbours
    for x, y in nearest_ngbh:
        if [y, x] in nearest_ngbh:
            mutual_pairs.append(x)
            mutual_pairs.append(y)
    return set(mutual_pairs)


step_size = 10**6
for n in range(3, 12):  # list containing different number of members/cars
    prob = 0
    for i in range(step_size):
        L = sorted([uniform(0, 1) for i in range(n)])
        random_car = choice(L)
        mutual_paired_cars = mutual_pair_finder(L)
        if random_car in mutual_paired_cars:
            prob += 1
    total_prob = prob / step_size
    print(n, ':', total_prob)
