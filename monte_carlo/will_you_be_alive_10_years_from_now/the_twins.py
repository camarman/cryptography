# Will you be alive in 10 years from now ?
# Problem 2: The Twins Problem

from random import shuffle

def twin_tester():
    """
    Testing if two twin sisters will end up in the same lab group of 20 people divided
    into 5 groups
    
    Args: 
        None
        
    Returns 
        [boolean]: True, if the teo twins are on the same group
    """
    students = [*[1]*2, *[0]*18]
    shuffle(students)
    for i in range(0, 20, 4):
        groups = students[i:i+4]
        if sum(groups) == 1:
            return False
        elif sum(groups) == 2:
            return True
    return False

counter = 0
for i in range(10**6):
    if twin_tester():
        counter += 1

prob = counter / 10**6
print(prob)
