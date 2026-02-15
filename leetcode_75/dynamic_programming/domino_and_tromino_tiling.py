"""
LeetCode 790: Domino and Tromino Tiling

Goal: count tilings of a 2 x n board using
- 1 x 2 dominoes, and
- L-shaped trominoes (3 squares).

State definition
----------------
dp[i] = number of ways to tile a 2 x i board.

Recurrence (editorial shortcut)
-------------------------------
Instead of summing many earlier states, we can use a simplified
recurrence:

    dp[i] = 2 * dp[i - 1] + dp[i - 3]

Quick intuition to remember this later:
- 2 * dp[i - 1]: either place a vertical domino on the last column,
  OR place two L-trominoes that "poke" into column i from i-1.
- dp[i - 3]: add the remaining pattern needed to cover the leftover
  protrusion.

Base cases
----------
dp[0] = 1 (empty board counts)
dp[1] = 1 (only vertical domino)
dp[2] = 2 (two vertical OR two horizontal dominoes)

"""

MOD = 10**9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        # Handle tiny boards directly (also avoids indexing issues).
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            # Use the editorial recurrence; always mod to prevent overflow.
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]
