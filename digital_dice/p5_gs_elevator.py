# Digital Dice
# Problem 5: The Gamow-Stern Elevator Puzzle

# something wrong with the solution/problem

from random import uniform
from math import ceil


def elevator_direction_generator():
    elevator_direction = uniform(0, 1)
    if elevator_direction > 0.5:
        return 'up'
    else:
        return 'down'


def elevator_floor_generator(direction):
    """Simulates the cycles of an elevator

    Args:
        pos [int]: the current floor of the elevator
        direction [string]: the direction of the elevator.

    Returns:
        [list]: the cycle of the elevator from the given initial position and direction
    """
    elevator_floor = uniform(0, 1)
    pos = ceil(6 * elevator_floor)
    cycle = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2]
    period = len(cycle)
    if pos == 1:
        direction = 'up'
    elif pos == 7:
        direction = 'down'
    if direction == 'up':
        return [cycle[(pos + i) % period] for i in range(15)]
    else:
        return [cycle[(period - pos + i) % period] for i in range(15)]


def elevators_direction(elevator_cycle, gamows_floor):
    index = elevator_cycle.index(gamows_floor)
    if elevator_cycle[index] < elevator_cycle[index + 1]:
        return 'up'
    else:
        return 'down'


gamows_floor = 2
gamows_direction = 'up'

down_counter = 0
for i in range(1):
    elevator1_direction = elevator_direction_generator()
    elevator_cycle = elevator_floor_generator(elevator1_direction)
    if elevators_direction(elevator_cycle, gamows_floor) == 'down':
        down_counter += 1

print(down_counter / 1)
