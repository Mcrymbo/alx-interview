#!/usr/bin/python3
"""module for calculating the number of coins change"""


def makeChange(coins, total):
    """function for calculating number of coins using
    dynamic programming algorithm """
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1
