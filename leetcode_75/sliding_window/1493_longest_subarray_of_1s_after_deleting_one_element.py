# LeetCode Problem 1493: Longest Subarray of 1's After Deleting One Element
# Sliding window approach: maintain start index of window after previous zero, update maximum window length.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_sa = 0
        s = 0
        zeroindex = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                s = zeroindex + 1
                zeroindex = i
            max_sa = max(max_sa, i - s)
        return max_sa
