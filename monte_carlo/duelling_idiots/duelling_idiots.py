from random import choice

a_wins = 0
sum_trigger = 0
max_trigger_num = 0
for i in range(10**6):
    chances = ["d", "nd", "nd", "nd", "nd", "nd"]  # nd = not dead, d = dead
    trigger_num = 0
    while True:
        b = choice(chances)  # A shoots B
        if b == "d":
            a_wins += 1
            trigger_num += 1
            break
        else:
            trigger_num += 1
            a = choice(chances)  # B shoots A
            if a == "d":
                trigger_num += 1
                break  # A cannot win
            else:
                trigger_num += 1
    if trigger_num > max_trigger_num:
        max_trigger_num = trigger_num
    sum_trigger += trigger_num

print("max trigger number =", max_trigger_num)
print("The probability that A wins =", a_wins / 10**6)
print("Average trigger number =", sum_trigger / 10**6)
