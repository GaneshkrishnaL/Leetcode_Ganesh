"""
LeetCode Problem 238: Product of Array Except Self
Difficulty: Medium
Topic: Array, Prefix Sum

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operator.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Solution Approach:
We use two passes to calculate prefix and suffix products:
1. First pass (left to right): Calculate prefix products
2. Second pass (right to left): Calculate suffix products and multiply with prefix

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) excluding the output array

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
- answer[0] = 2*3*4 = 24
- answer[1] = 1*3*4 = 12
- answer[2] = 1*2*4 = 8
- answer[3] = 1*2*3 = 6

Author: Ganesh Krishna Lakshmisetty
Date: December 07, 2025
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate the product of all elements except self for each index.
        
        Args:
            nums: List[int] - Input array of integers
            
        Returns:
            List[int] - Array where each element is the product of all other elements
        """
        # Get the length of the input array
        array_length = len(nums)
        
        # Initialize result array with all 1s
        # This will store the final products
        result = [1] * array_length
        
        # Variable to store the running product from left to right
        prefix_product = 1
        
        # First pass: Calculate prefix products (product of all elements to the left)
        # For each index i, result[i] will contain the product of all elements before i
        for index in range(array_length):  # [1,2,3,4] -> indices 0,1,2,3
            result[index] = prefix_product  # result = [1, 1, 2, 6]
            prefix_product = prefix_product * nums[index]  # prefix_product = 1, 2, 6, 24
        
        # Variable to store the running product from right to left
        suffix_product = 1
        
        # Second pass: Calculate suffix products (product of all elements to the right)
        # Multiply the existing prefix product with suffix product
        for index in range(array_length - 1, -1, -1):  # [1,2,3,4] -> indices 3,2,1,0
            result[index] = result[index] * suffix_product  # result = [24, 12, 8, 6]
            suffix_product = suffix_product * nums[index]  # suffix_product = 4, 12, 24, 24
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    test_input_1 = [1, 2, 3, 4]
    expected_output_1 = [24, 12, 8, 6]
    actual_output_1 = solution.productExceptSelf(test_input_1)
    print(f"Test 1: Input: {test_input_1}")
    print(f"Expected: {expected_output_1}")
    print(f"Actual: {actual_output_1}")
    print(f"Pass: {actual_output_1 == expected_output_1}\n")
    
    # Test case 2
    test_input_2 = [-1, 1, 0, -3, 3]
    expected_output_2 = [0, 0, 9, 0, 0]
    actual_output_2 = solution.productExceptSelf(test_input_2)
    print(f"Test 2: Input: {test_input_2}")
    print(f"Expected: {expected_output_2}")
    print(f"Actual: {actual_output_2}")
    print(f"Pass: {actual_output_2 == expected_output_2}")
