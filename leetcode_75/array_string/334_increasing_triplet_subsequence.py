"""
LeetCode 334: Increasing Triplet Subsequence  

Given an integer array nums, return True if there exists a triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k], else False.  

This solution uses a greedy O(n) time and O(1) space algorithm:
 - We maintain two variables, `first` and `second`, representing the smallest and second smallest numbers found so far.  
 - When we see a number x:  
    * If x <= first, we update first.  
    * Else if x <= second, we update second.  
    * Else x > first and x > second, so we found a triplet: first < second < x.  
The key insight is that `first` and `second` don't store the final triplet values, but act as evidence that an increasing subsequence of length 2 exists somewhere before x. When we find x bigger than both, the triplet must exist in the array (even if first and second were updated later).  
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Determine if the input list contains an increasing triplet subsequence.  

        Args:
            nums (List[int]): The list of integers to search.  

        Returns:
            bool: True if there exist indices i < j < k such that  
                  nums[i] < nums[j] < nums[k], otherwise False.  

        The algorithm runs in O(n) time and uses O(1) extra space.  
        """
        # Initialize first and second to positive infinity.  
        # `first` will hold the smallest number seen so far.  
        # `second` will hold the smallest number > first seen so far.  
        first = float('inf')
        second = float('inf')

        # Iterate through each number in the array.  
        for x in nums:
            if x <= first:
                # We found a new smallest number. Update `first`.  
                # Even if this number appears later in the array,  
                # setting `first` here ensures it is as small as possible.  
                first = x
            elif x <= second:
                # We found a number greater than `first` but smaller than or equal to `second`.  
                # This means we have an increasing pair (first, x). Update `second` to this value.  
                second = x
            else:
                # If we find a number greater than both `first` and `second`,  
                # we have confirmed the existence of an increasing triplet.  
                return True

        # If we finish iterating without finding such a triplet, return False.  
        return False
