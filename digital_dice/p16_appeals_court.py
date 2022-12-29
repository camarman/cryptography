# Digital Dice
# Problem 16: The Appeals Court Paradox

from random import uniform


def random_case_generator():
    """
    Creating random cases where the criminal is either truly innocent or truly guilty

    Returns:
        [string]: The true nature of the criminal
    """
    if uniform(0, 1) < 0.5:
        return 'innocent'
    else:
        return 'guilty'


def judge_vote(p, true_case):
    """
    Calculating the individual votes of the judge

    Args:
        p [float]: The probability that the judge makes correct decisions
        true_case [string]: The true nature of the criminal

    Returns:
        [string]: The vote of the judge
    """
    if true_case == 'innocent':
        if uniform(0, 1) < p:
            return 'innocent'
        else:
            return 'guilty'
    else:
        if uniform(0, 1) < p:
            return 'guilty'
        else:
            return 'innocent'


def judge_resultA(true_case, pA, pB, pC, pD, pE):
    """
    The final result of the judges. Every judge votes individually (part A) 

    Args:
        true_case [string]: The true nature of the criminal
        pA [float]: The probability that the judge A makes correct decision
        pB [float]: The probability that the judge B makes correct decision
        pC [float]: The probability that the judge C makes correct decision
        pD [float]: The probability that the judge D makes correct decision
        pE [float]: The probability that the judge E makes correct decision

    Returns:
        [string]: The result of the voting
    """
    judge_p_values = [pA, pB, pC, pD, pE]
    total_votes = [judge_vote(p, true_case) for p in judge_p_values]
    votes_innocent = total_votes.count('innocent')
    votes_guilty = total_votes.count('guilty')
    if votes_innocent > votes_guilty:
        return 'innocent'
    else:
        return 'guilty'


def judge_resultB(true_case, pA, pB, pC, pD):
    """
    The final result of the judges. Judge E votes as the same as Judge A (part B)

    Args:
        true_case [string]: The true nature of the criminal
        pA [float]: The probability that the judge A makes correct decision
        pB [float]: The probability that the judge B makes correct decision
        pC [float]: The probability that the judge C makes correct decision
        pD [float]: The probability that the judge D makes correct decision

    Returns:
        [string]: The result of the voting
    """
    judge_p_values = [pA, pB, pC, pD]
    votes_without_E = [judge_vote(p, true_case) for p in judge_p_values]
    total_votes = votes_without_E + [votes_without_E[0]] #judge E votes the same as judge A
    votes_innocent = total_votes.count('innocent')
    votes_guilty = total_votes.count('guilty')
    if votes_innocent > votes_guilty:
        return 'innocent'
    else:
        return 'guilty'

total_case = 10**6

##### Part A ####
# # Judge E votes independently


# incorrect_decisionA = 0
# for case_num in range(total_case):
#     true_case = random_case_generator()
#     if true_case != judge_resultA(true_case, 0.95, 0.95, 0.90, 0.90, 0.80):
#         incorrect_decisionA += 1
# print(incorrect_decisionA / total_case)

##### Part B ####
# Judge E votes the same as Judge A

incorrect_decisionB = 0
for case_num in range(total_case):
    true_case = random_case_generator()
    if true_case != judge_resultB(true_case, 0.95, 0.95, 0.90, 0.90):
        incorrect_decisionB += 1

print(incorrect_decisionB / total_case)
