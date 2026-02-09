# This solution finds the single number using bit manipulation.
# It iterates through the list and applies XOR so that pairs cancel out.
# The remaining number after XORing all elements is the single one.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Return the element that appears only once in the list.
        Uses XOR to cancel out pairs of identical numbers, leaving the unique number.
        """
        result = 0
        for num in nums:
            result ^= num
        return result
