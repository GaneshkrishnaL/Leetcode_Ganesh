"""
LeetCode 724 - Find Pivot Index
This problem asks us to find the leftmost index in an integer array such that the sum of all elements to the left of the index is equal to the sum of all elements to the right. If no such index exists, return -1.

Approach:
- Compute the total sum of the array (rightsum) at the start.
- Iterate through the array using an index i.
- At each index:
    * Subtract the current number from rightsum to represent the sum of elements to the right of i.
    * If leftsum equals rightsum, we have found the pivot index; return i.
    * Add the current number to leftsum for the next iteration.
- If no index satisfies the condition, return -1.

Time Complexity: O(n) because we traverse the list once and sum once.
Space Complexity: O(1) since we use a few extra variables.

"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Returns the pivot index of the array where the sum of numbers to the left 
        of the index is equal to the sum of numbers to the right of the index.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The leftmost pivot index if it exists, otherwise -1.
        """
        # Initialize left sum to 0 since there are no elements to the left initially
        leftsum = 0
        # Compute the total sum of the list, this will serve as the running right sum
        rightsum = sum(nums)

        # Iterate over each element by index
        for i in range(len(nums)):
            # The current element is no longer part of the right side, subtract it
            rightsum -= nums[i]
            # If the sums on both sides match, we found the pivot
            if leftsum == rightsum:
                return i
            # Otherwise, include the current element in the left sum for next iteration
            leftsum += nums[i]
        
        # If no pivot index is found, return -1
        return -1
