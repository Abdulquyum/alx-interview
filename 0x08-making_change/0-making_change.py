#!/usr/bin/python3
"""
Determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins: int, total: int) -> int:
    """ Determine the fewest number of coins needed to meet a given total """
    if total <= 0:
        return 0

    minimum_coins = [float('inf')] * (total + 1)
    minimum_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            minimum_coins[i] = min(minimum_coins[i],
                                   minimum_coins[i - coin] + 1)

    if minimum_coins[total] != float('inf'):
        return (minimum_coins[total])
    return (-1)
