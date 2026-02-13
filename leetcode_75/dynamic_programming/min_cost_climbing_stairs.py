"""
LeetCode 746: Min Cost Climbing Stairs

This module provides a function to compute the minimum cost required to reach the top of a staircase,
given an array of costs where each element represents the cost to step on that stair. You can either
climb one or two steps at a time. The objective is to minimize the total cost incurred when reaching
the top (beyond the last index).

The dynamic programming approach defines dp[i] as the minimum cost to reach step i. Since you can come
from step i-1 or i-2, the recurrence relation is:

    dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

with base cases dp[0] = 0 and dp[1] = 0. The answer is dp[n] where n is len(cost).
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Return the minimum cost to reach the top of the stairs.

        Args:
            cost (List[int]): A list where cost[i] is the cost of stepping on step i.

        Returns:
            int: The minimum total cost to reach the top of the staircase.
        """
        n = len(cost)
        # dp array to store the minimum cost to reach each step, with an extra space for the top
        dp = [0] * (n + 1)

        # Base cases: starting from step 0 or step 1 costs nothing
        dp[0] = 0
        dp[1] = 0

        # Build the dp array using the recurrence relation
        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],  # Take one step from (i-1)
                dp[i - 2] + cost[i - 2]   # Take two steps from (i-2)
            )

        # The value at dp[n] gives the minimum cost to reach the top
        return dp[n]
