"""
283. Move Zeroes

Given an integer array nums, move all zeros to the end of the array while maintaining the relative order of the non-zero elements.

Solution Explanation:
- We use two pointers: 'i' to mark the position where the next non-zero element should go, and 'ix' to traverse the array.
- When nums[ix] is non-zero, we swap nums[i] and nums[ix]. This brings the non-zero element forward.
- We then increment i to point to the next position for a non-zero element.
- Regardless of whether we swapped, we increment ix to examine the next element.
- This operates in-place with O(n) time and O(1) space.

Example:
nums = [0, 1, 0, 3, 12]
During traversal:
- ix=0: nums[0] is 0 (skip)
- ix=1: nums[1]=1, swap with nums[0], array becomes [1,0,0,3,12], i moves to 1
- ix=2: nums[2]=0 skip
- ix=3: nums[3]=3, swap nums[1] and nums[3], array becomes [1,3,0,0,12], i=2
- ix=4: nums[4]=12, swap nums[2] and nums[4], array becomes [1,3,12,0,0], i=3

After the loop, all non-zero elements are at the front in original order and zeros moved to the end.
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zero elements in 'nums' to the end while preserving the
        order of non-zero elements. This modifies 'nums' in place.

        Args:
            nums (List[int]): The list of integers to be rearranged.

        Returns:
            None: The function modifies the list in place and returns nothing.
        """
        # Pointer 'i' tracks the index where the next non-zero element should be placed.
        i = 0

        # Pointer 'ix' traverses the array to find non-zero elements.
        ix = 0

        # Iterate until 'ix' reaches the end of the list.
        while ix < len(nums):
            # If the current element is not zero, bring it forward.
            if nums[ix] != 0:
                # Swap the non-zero element at index 'ix' with the element at index 'i'.
                # This moves the non-zero element to its correct position at the front.
                nums[i], nums[ix] = nums[ix], nums[i]

                # After placing a non-zero element, increment 'i' to the next position.
                i += 1

            # Always move to the next element in the array.
            ix += 1

        # No explicit return is needed since the operation modifies the list in place.
