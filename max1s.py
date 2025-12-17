from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_ones = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1

            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

            max_ones = max(max_ones, end - start + 1)

        return max_ones