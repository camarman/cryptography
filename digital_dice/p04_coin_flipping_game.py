# Digital Dice
# Problem 4: A Curious Coin-Flipping Game

from random import choice


def coin_comparison(coin_types, coin_num_l, coin_num_m, coin_num_n):
    """
    Determining the coin number after a single toss

    Args:
        coin_types [list]: The type of the coin as 'TTH', 'HHH', 'THH' etc.
        coin_num_l [int]: The number of the coins that player 'l' has
        coin_num_m [int]: The number of the coins that player 'm' has
        coin_num_n [int]: The number of the coins that player 'n' has

    Returns:
        The number of coins for the each player
    """
    if coin_types[0] == coin_types[1] == coin_types[2]:  # if TTT or HHH
        return False
    elif coin_types[0] == coin_types[1]:  # if HHT or TTH
        coin_num_l += -1
        coin_num_m += -1
        coin_num_n += 2
        return coin_num_l, coin_num_m, coin_num_n
    elif coin_types[0] == coin_types[2]:  # if HTH or THT
        coin_num_l += -1
        coin_num_m += 2
        coin_num_n += -1
        return coin_num_l, coin_num_m, coin_num_n
    elif coin_types[1] == coin_types[2]:  # if THH or HHT
        coin_num_l += 2
        coin_num_m += -1
        coin_num_n += -1
        return coin_num_l, coin_num_m, coin_num_n


def single_game(coin, coin_num_l, coin_num_m, coin_num_n):
    """
    Returns the toss number when a player losses the game

    Args:
        coin_num_l [int]: The number of the coins that player 'l' has
        coin_num_m [int]: The number of the coins that player 'm' has
        coin_num_n [int]: The number of the coins that player 'n' has

    Returns:
        [int]: the toss number until a player losses
    """
    toss_num = 0
    while coin_num_n > 0 and coin_num_m > 0 and coin_num_l > 0:
        coin_types = [choice(coin) for i in range(3)]
        N = coin_comparison(coin_types, coin_num_l, coin_num_m, coin_num_n)
        if not N:
            toss_num += 1
        else:
            coin_num_l = N[0]
            coin_num_m = N[1]
            coin_num_n = N[2]
            toss_num += 1
    return toss_num


coin_num_l = float(input("The coin number for player 1: "))
coin_num_m = float(input("The coin number for player m: "))
coin_num_n = float(input("The coin number for player n: "))
p = float(input("The fairness of the coin (0 - 1):"))

# Some calculations to change the fairness of the coin
updated_p = int((str(p)[2:]))
digits = len(str(p)[2:])
coin = ['H'] * updated_p + ['T'] * (10**digits-updated_p)

step_size = 10**6
toss_num_total = 0
for i in range(step_size):
    toss_num_total += single_game(coin, coin_num_l, coin_num_m, coin_num_n)
print(toss_num_total / step_size)
