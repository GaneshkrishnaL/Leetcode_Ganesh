# 605. Can Place Flowers solution with detailed explanation
#
# Problem Description:
# You are given an integer array `flowerbed` containing 0s and 1s, where 0 means empty and 1 means not empty, and an integer `n`.
# We need to determine if `n` new flowers can be planted in the `flowerbed` without violating the rule that no two flowers can be adjacent.
#
# Approach:
# - We iterate through each position in the flowerbed.
# - For each position, we check three conditions to decide if we can plant a flower there:
#   1. The current position is empty (flowerbed[i] == 0).
#   2. The left neighbor is empty or the current position is the first plot.
#   3. The right neighbor is empty or the current position is the last plot.
# - If all three conditions are satisfied, we plant a flower by setting flowerbed[i] = 1 and increment our count of planted flowers.
# - If at any point the count of planted flowers equals or exceeds `n`, we can return True early since we've satisfied the requirement.
# - After checking all plots, if the count of planted flowers is still less than `n`, we return False.
#
# This solution runs in O(m) time where m is the length of the flowerbed, since we traverse it once. The space complexity is O(1) as we only use a few variables.

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determine if it's possible to plant `n` new flowers in the flowerbed without violating the no-adjacent-flowers rule.

        Parameters:
        flowerbed (List[int]): List representing the flowerbed where 0 means empty and 1 means there is already a flower.
        n (int): Number of new flowers that need to be planted.

        Returns:
        bool: True if `n` flowers can be planted, False otherwise.
        """
        # Count of flowers planted so far
        count = 0

        # Iterate over each position in the flowerbed
        for i in range(len(flowerbed)):
            # Check if current position is empty
            if flowerbed[i] == 0:
                # Check if left neighbor is empty or we are at the beginning
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if right neighbor is empty or we are at the end
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both left and right neighbors are empty, we can plant here
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant a flower at the current position
                    count += 1       # Increment the planted flower count

                    # If we've planted enough flowers, return True early
                    if count >= n:
                        return True

        # If we've finished checking all positions, return whether we planted enough flowers
        return count >= n
