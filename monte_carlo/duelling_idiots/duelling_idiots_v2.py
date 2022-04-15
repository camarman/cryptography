from random import choice

chances = ["d", "nd", "nd", "nd", "nd", "nd"]


def shoots(chances, trigger_num):
    for i in range(trigger_num):
        person = choice(chances)
        if person == "d":
            return True


a_wins = 0
for i in range(10 ** 6):
    trigger_num = 1
    while True:
        A = shoots(chances, trigger_num)
        if A:
            a_wins += 1
            break
        else:
            trigger_num += 1
            B = shoots(chances, trigger_num)
            if B:
                break
            else:
                trigger_num += 1

print(a_wins / 10 ** 6)
