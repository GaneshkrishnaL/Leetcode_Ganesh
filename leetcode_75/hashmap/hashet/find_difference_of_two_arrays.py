"""
Solution for the problem of finding the difference of two arrays.

Given two integer arrays nums1 and nums2, we need to return a list containing two lists:
  1. A list of all distinct integers present in nums1 but not in nums2.
  2. A list of all distinct integers present in nums2 but not in nums1.

This implementation converts each input list to a set to remove duplicates and then uses set difference operations
to compute the required values.

Time Complexity:
- Converting each list to a set takes O(n + m) time, where n and m are the lengths of nums1 and nums2, respectively.
- Performing set difference operations is O(n + m) in total.
- Converting the resulting sets back to lists is O(k) where k is the number of distinct differences.

Overall, the solution runs in linear time with respect to the sizes of the input lists.

Space Complexity:
- We use additional space proportional to the number of distinct elements in nums1 and nums2 to store the sets.

Author: Ganesh
Date: December 19, 2025
"""

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Find distinct elements in nums1 not in nums2 and in nums2 not in nums1.

        Args:
            nums1 (List[int]): The first list of integers.
            nums2 (List[int]): The second list of integers.

        Returns:
            List[List[int]]: A list where:
                - index 0 holds a list of distinct integers present in nums1 but not in nums2.
                - index 1 holds a list of distinct integers present in nums2 but not in nums1.
        """

        # Convert the input lists to sets to eliminate duplicates and allow efficient difference operations.
        set1 = set(nums1)
        set2 = set(nums2)

        # Compute the difference: elements in set1 that are not in set2.
        diff1 = list(set1 - set2)

        # Compute the difference: elements in set2 that are not in set1.
        diff2 = list(set2 - set1)

        # Return the two differences as a list of lists.
        return [diff1, diff2]
