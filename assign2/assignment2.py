"""
Name: Poon Yeong Shian
ID: 30696003
"""
import math


# Q1
def count_encounters(target_difficulty, monster_list):
    """
    # referred to the https://www.geeksforgeeks.org/coin-change-dp-7/, viewed on 1th Sep 2021
    This function give out how many different possible encounters there are which satisfy this target difficulty
    :param target_difficulty: level difficulty
    :param monster_list: a list of tuple which contains monster and its level
    :return: number of combinations
    :complexity:
        time: O(DM), D is the value of target_difficulty,
                     M is the length of monster_list
        space: O(D), D is the value of target_difficulty
    """
    # initialise row and col
    row = len(monster_list)
    col = target_difficulty

    if target_difficulty == 0:
        return 1

    # initialise memo
    memo = [0 for _ in range(col + 1)]

    # Base case
    memo[0] = 1

    # loop through the monster list
    for row in range(row):
        # loop through memo
        # update memo with the sum of memo[index], (index is the current value - the monster level selected),
        # monster level selected is smaller than or equal to the current value
        for col in range(monster_list[row][1], col + 1):
            memo[col] += memo[col - monster_list[row][1]]

    return memo[col]


# Q2
def best_lamp_allocation(num_p, num_l, probs):
    """
    This function return an float, which is the highest probability of all plants being ready by the party that can
    be obtained by allocating lamps to plants optimally.
    :param num_p: plant number
    :param num_l: number of lamp
    :param probs: probs is a list of lists, where probs[i][j] represents the probability that plant i will be ready
                  in time if it is allocated j lamps
    :return: an float, which is the highest probability of all plants being ready by the party that can be obtained
             by allocating lamps to plants optimally
    :complexity:
        time: O(PL^2), P is num_p, and L is num_l
        space: O(PL), P is num_p, and L is num_l
    """
    m = num_l
    n = num_p

    if len(probs) == 0:
        return 1

    # base case first row of memo is 0
    # initialize all memo matrix as 0
    memo = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # copy the 1st row of probs into 2nd row of the memo
    for j in range(m + 1):
        memo[1][j] = probs[0][j]

    # create a list of possible remaining lamps at that num_plant
    remaining = [s for s in range(m, -1, -1)]
    # loop num_plant, start from 2
    for col in range(2, n + 1):
        # loop every lamp
        for row in range(m + 1):
            # create a temporary lst
            lst = []
            # loop the possible remain
            for k in range(remaining[row] + 1):
                temp = probs[col - 1][row] * memo[col - 1][k]
                # maximum is the optimal probability at the current plant and lamp
                lst.append(temp)

            if len(lst) != 0:
                # get the max and index of maximum probability then minus remaining
                maximum = max(lst)
                max_index = lst.index(maximum)
                remaining[row] -= max_index
                memo[col][row] = maximum
            else:
                # get previous plant and multiple by previous prob
                memo[col][row] = probs[col - 1][row] * memo[col - 1][row]
    # the highest probability of all plants, by allocating lamps to plants optimally
    return max(memo[num_p])
