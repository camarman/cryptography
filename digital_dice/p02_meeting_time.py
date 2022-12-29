# Digital Dice
# Problem 2: Will Lil and Bill Meet at the Malt Shop?

from random import uniform


def meeting(lils_waiting_time, bills_waiting_time, waiting_interval):
    """
    Investigating the condition where the Lil and Bill meet or not

    Args:
        lils_waiting_time [int]: Lil's waiting time in minutes
        bills_waiting_time [int]: Bill's waiting time in minutes
        waiting_interval [int]: the meeting interval in minutes

    Returns:
        True if they ever meet, otherwise returns False
    """
    lils_mt = uniform(0, 1)
    bills_mt = uniform(0, 1)
    if lils_mt < bills_mt < lils_mt + lils_waiting_time / waiting_interval:  # Lil arrives first and waits 5 min
        return True
    elif bills_mt < lils_mt < bills_mt + bills_waiting_time / waiting_interval:  # Bill arrives first and waits 7 min
        return True


step_size = 10**7
meeting_counter = 0
for i in range(step_size):
    if meeting(5, 7, 30):
        # if meeting(5, 5, 30):
        # if meeting(7, 7, 30):
        meeting_counter += 1
print(meeting_counter / step_size)
