import math


def coin_exchange2(value, coins):
    memo = [-1] * (value + 1)
    memo[0] = 0
    if memo[value] != -1:
        return memo[value]
    else:
        minCoins = math.inf
        for i in range(1, len(coins)):
            if coins[i] <= value:
                c = 1 + coin_exchange2(value - coins[i])
                if c < minCoins:
                    minCoins = c
        memo[value] = minCoins
    return memo[value]


def backtracking(list1, target):
    ret = []
    list2 = [i for i in range(target + 1)]

    while target != 0:
        ret.append(list1[target])
        target = list2[target] - list1[target]
    return ret


def coin_exchange(n, coin):
    m = len(coin)
    memo = [math.inf] * (n + 1)
    memo[0] = 0
    for value in range(1, n + 1):
        new_list2 = []
        for j in range(m):
            if coin[j] <= value:
                balance = value - coin[j]
                count = 1 + memo[balance]
                if count < memo[value]:
                    memo[value] = count

    return memo


# print(coin_exchange(5, [1, 5, 6, 9]))

# print(coin_exchange(12, [1, 5, 6, 9]))

N = 4

# function find maximum sum path
R = 3
C = 3

import sys


# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]
R = 3
C = 3


def minCost(cost, m, n):
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]
    print(tc)
    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]
    print(tc)
    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]

    return tc[m][n]


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, 2, 2))


