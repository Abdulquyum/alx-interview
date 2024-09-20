#!/usr/bin/env python3
""" Determine the fewest number of coins needed to meet a given amount total """

def makeChange(coins: int, total: int) -> int:
""" Determine the fewest number of coins needed to meet a given total """
if total <= 0:
    return 0

# Initialize a list to store the minimum coins needed for each amount
dp = [float('inf')] * (total + 1)
dp[0] = 0  # No coins needed to make 0 total

for i in range(1, total + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

return dp[total] if dp[total] != float('inf') else -1
