#!/usr/bin/python3
"""
Module that calculates the fewest number of operations
"""


def minOperations(n):
    if n == 1:
        return 0

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n] if dp[n] != float('inf') else 0
