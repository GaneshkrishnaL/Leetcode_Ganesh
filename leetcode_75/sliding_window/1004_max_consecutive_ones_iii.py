"""
LeetCode Problem 1004: Max Consecutive Ones III
This solution uses the sliding window technique to find the longest contiguous subarray 
containing at most k zeros (i.e., flipping at most k zeros to ones).
The window expands with the right pointer; if the number of zeros exceeds k, 
the left pointer moves rightwards until the window again contains at most k zeros. 
The length of the window is tracked to obtain the maximum possible.
Time Complexity: O(n), where n is the length of nums, since each index is visited at most twice.
Space Complexity: O(1), since only a few integer counters are used regardless of input size.
"""

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Returns the length of the longest subarray containing at most k zeroes.
        
        Args:
            nums (List[int]): List of binary digits (0s and 1s).
            k (int): Maximum number of zeros that can be flipped to ones.
        
        Returns:
            int: Maximum length of a subarray with at most k zero flips.
        """
        left = 0  # Left pointer of the sliding window
        zeros = 0  # Count of zeros in the current window
        max_len = 0  # Maximum length of a valid window found so far
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # If current element is zero, increment the zero count
            if nums[right] == 0:
                zeros += 1
            
            # If zero count exceeds k, shrink the window from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # Move left pointer to the right
            
            # Update the maximum length with the current window size
            current_window_size = right - left + 1
            if current_window_size > max_len:
                max_len = current_window_size
        
        return max_len
