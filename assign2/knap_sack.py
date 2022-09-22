import math


def knap_sack(weight, value, n):
    m = len(weight)

    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):  # m = 2
        for j in range(1, n + 1):  # n = 1
            exclude = memo[i - 1][j]
            include = 0
            if weight[i - 1] <= j:  # i is weight[i]
                include = value[i - 1] + memo[i - 1][j - weight[i - 1]]
            memo[i][j] = max(include, exclude)
    return memo[m][n]


# weight1 = [6, 1, 5, 9]
# value1 = [230, 40, 350, 550]
#
# print(knap_sack(weight1,value1, 12))


# def coin_exchange(n, coin):
#     m = len(coin)
#     memo = [math.inf] * (n + 1)
#     memo[0] = 0
#     for value in range(1, n + 1):
#         for j in range(m):
#             if coin[j] <= value:
#                 balance = value - coin[j]
#                 count = 1 + memo[balance]
#                 if count < memo[value]:
#                     memo[value] = count
#     return memo
#
#
# print(coin_exchange(12, [1, 5, 6, 9]))

def count_encounters(target_difficulty, monster_list):
    """
    references:https://www.geeksforgeeks.org/coin-change-dp-7/
    :param target_difficulty:
    :param monster_list:
    :return:
    """
    m = len(monster_list)
    n = target_difficulty

    if target_difficulty == 0:
        return 0
    # initialise memo
    memo = [[0 for _ in range(n + 1)] for _ in range(m)]

    # pre-sort the monster_list according to level
    monster_list = sorted(monster_list, key=lambda x: x[1])

    # Fill the first col with 1
    for k in range(m):
        memo[k][0] = 1

    # loop through level
    for i in range(1, n + 1):
        # loop through monster list
        for j in range(m):
            # Number of combinations including monster_list[j]
            if i - monster_list[j][1] >= 0:
                x = memo[j][i - monster_list[j][1]]
            else:
                x = 0

            # Number of combinations excluding monster_list[j]
            if j >= 1:
                y = memo[j - 1][i]
            else:
                y = 0

            # total combination
            memo[j][i] = x + y
    print(memo)
    return memo[m - 1][n]


# target_difficulty1 = 4
# monster_list1 = [("bear", 1), ("imp", 2),("imp", 2), ("kobold", 3)]
# print(count_encounters(target_difficulty1, monster_list1))

def best_lamp_allocation(num_p, num_l, probs):
    m = num_l
    n = num_p
    memo = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for j in range(m + 1):
        memo[1][j] = probs[0][j]

    for col in range(2, m + 1):
        for row in range(n + 1):
            maximum = 0
            for k in range(num_l - row, -1, -1):
                temp = probs[col - 1][row] * memo[col - 1][k]
                if temp > maximum:
                    maximum = temp
            memo[col][row] = maximum

    max_prob = 0
    for i in range(len(memo)):
        temp3 = max(memo[i])
        if max_prob < temp3:
            max_prob = temp3

    return max(memo[num_l])


probs = [[0.5, 0.5, 1], [0.25, 0.1, 0.75]]
print(best_lamp_allocation(2, 2, probs))

probs = [[0.5, 0.75, 0.25], [0.75, 0.25, 0.8]]
print(best_lamp_allocation(2, 2, probs))

probs = [[0.39, 0.53, 0.09, 0.13, 0.36, 0.91, 0.84, 0.14, 0.3, 0.23, 0.21],
         [0.31, 0.49, 0.99, 0.13, 0.45, 0.7, 0.73, 0.22, 0.97, 0.89, 0.93],
         [0.08, 0.73, 0.17, 0.24, 0.62, 0.69, 0.43, 0.31, 0.79, 0.73, 0.96],
         [0.42, 0.1, 0.97, 0.27, 0.5, 0.84, 0.32, 0.53, 0.31, 0.22, 0.93],
         [0.45, 0.51, 0.99, 0.86, 0.22, 0.62, 0.45, 0.47, 0.83, 0.88, 0.85],
         [0.68, 0.35, 0.5, 0.06, 0.14, 0.88, 0.51, 0.84, 0.35, 0.12, 0.38],
         [0.86, 0.64, 0.78, 0.17, 0.24, 0.69, 0.4, 0.72, 0.74, 0.14, 0.97],
         [0.48, 0.02, 0.48, 0.09, 0.73, 0.37, 0.68, 0.34, 0.49, 0.28, 0.37],
         [0.69, 0.25, 0.46, 0.2, 0.68, 0.73, 0.83, 0.26, 0.92, 0.74, 0.97],
         [1.0, 0.57, 0.77, 0.55, 0.79, 0.54, 0.07, 0.89, 0.38, 0.55, 0.87]]
print(best_lamp_allocation(10, 10, probs))
# ok
# num_p2 = 3
# num_l2 = 4
# probs = [[0.84, 0.76, 0.42, 0.26, 0.51], [0.4, 0.78, 0.3, 0.48, 0.58], [0.91, 0.5, 0.28, 0.76, 0.62]]
# best_lamp_allocation(num_p2, num_l2, probs)

# ok
# num_p3 = 4
# num_l3 = 2
# probs3 = [[0.8, 0.8, 0.4], [0.3, 0.5, 0.4], [0.8, 0.3, 0.5], [0.6, 0.9, 0.5]]
# best_lamp_allocation(num_p3, num_l3, probs3)


def MaximumPath(Mat):
    result = 0
    n = len(Mat)
    m = len(Mat[0])

    num_lamp = len(Mat[0]) - 1

    # create 2D matrix to store the sum
    # of the path
    # initialize all dp matrix as '0'
    dp = [[0 for _ in range(m + 2)] for _ in range(n)]

    path = [0]
    for t in range(m, -1, -1):
        path.append(t)

    # print(path)
    print(dp)
    # copy all element of first column into
    # dp first column
    for i in range(n):
        for j in range(1, m + 1):
            if i == 0:
                lst = [dp[i - 1][k] for k in range(1, m + 1)]
                dp[i][j] = max(lst) * \
                           Mat[i][j - 1]
            else:
                path[j] -= j
                lst = [dp[i - 1][k] for k in range(1, m + 1)]
                dp[i][j] = max(lst) * \
                           Mat[i][j - 1]

    print(path)
    # Find maximum path sum that end ups
    # at any column of last row 'N-1'
    for i in range(m + 1):
        result = max(result, dp[n - 1][i])
    print(dp)
    # return maximum sum path
    return result


# # driver program to test above function
# Mat = [[4, 2, 3, 4],
#        [2, 9, 1, 10],
#        [15, 1, 3, 0],
#        [16, 92, 41, 44]]
#
# # n = 4
# # m = 5
# print(MaximumPath(Mat))

def best_lamp_allocation(num_p, num_l, probs):
    dp = [[0 for _ in range(num_l + 1)] for _ in range(num_p + 1)]
    print(dp)
    for i in range(len(dp)):
        dp[0][i] = 1
    print(dp)

    for i in range(1, num_l + 1):
        for j in range(num_p + 1):
            # for k in range(len(probs)):
            print(probs[i - 1][j])
            # print(i,j)
            # dp[i][j] *= probs[i-1][j]


prob = [[0.5, 0.75, 0.25], [0.75, 0.25, 0.8]]
# print(prob)
# best_lamp_allocation(2, 2, prob)
