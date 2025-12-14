"""
LeetCode 643: Maximum Average Subarray I
Difficulty: Easy
Topic: Sliding Window, Array

Problem Statement:
-----------------
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach: Sliding Window Technique
----------------------------------
The sliding window technique is optimal for this problem because:
1. We need to find the maximum sum of k consecutive elements
2. Instead of recalculating sum for each window (O(n*k)), we slide the window (O(n))
3. When window slides right: add new element, remove leftmost element

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only using a few variables

Algorithm Steps:
1. Calculate sum of first k elements (initial window)
2. Set maxsum = initial window sum
3. Slide window from index k to n-1:
   - Add the new element entering the window (nums[i])
   - Remove the element leaving the window (nums[i-k])
   - Update maxsum if current sum is larger
4. Return maxsum / k as the maximum average
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Find maximum average of any contiguous subarray of length k.
        
        Args:
            nums: List of integers
            k: Length of subarray
            
        Returns:
            float: Maximum average value
        """
        # Step 1: Calculate sum of the first window (first k elements)
        # Using Python's slice notation for clarity
        # This initializes our sliding window
        summ = sum(nums[:k])
        
        # Step 2: Initialize maxsum with the first window's sum
        # This represents the best sum we've found so far
        maxsum = summ
        
        # Step 3: Slide the window from index k to end of array
        # Each iteration moves the window one position to the right
        for i in range(k, len(nums)):
            # Sliding window update in O(1) time:
            # Add the new element entering the window from right
            summ += nums[i]
            
            # Remove the element leaving the window from left
            # The element at index (i-k) is now outside our k-sized window
            summ -= nums[i - k]
            
            # Update maxsum if current window sum is larger
            # This keeps track of the best sum across all windows
            maxsum = max(maxsum, summ)
        
        # Step 4: Return the maximum average
        # Divide maxsum by k to get the average
        return maxsum / k


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    result1 = solution.findMaxAverage(nums1, k1)
    print(f"Test 1: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: 12.75000\n")
    
    # Test Case 2
    nums2 = [5]
    k2 = 1
    result2 = solution.findMaxAverage(nums2, k2)
    print(f"Test 2: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: 5.00000\n")
    
    # Test Case 3 - All negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    result3 = solution.findMaxAverage(nums3, k3)
    print(f"Test 3: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: -1.5 (window [-1, -2])\n")

"""
Key Insights:
-------------
1. Sliding Window Optimization:
   - Naive approach: Recalculate sum for each window → O(n*k)
   - Sliding window: Update sum incrementally → O(n)
   - Space efficient: Only stores sum variables

2. Edge Cases Handled:
   - Single element array (k=1): Returns that element
   - All negative numbers: Correctly finds max (least negative) average
   - k equals array length: Returns average of entire array

3. Common Mistakes to Avoid:
   - Don't reset summ to 0 in the loop (accumulate the changes)
   - Remember to divide by k at the end (return average, not sum)
   - Use maxsum to track best sum, not best average (avoid repeated divisions)

4. Performance:
   - Runtime: 82 ms (Beats 60.19%)
   - Memory: 27.35 MB (Beats 51.58%)

Related Problems:
-----------------
- LeetCode 209: Minimum Size Subarray Sum
- LeetCode 424: Longest Repeating Character Replacement
- LeetCode 713: Subarray Product Less Than K
- LeetCode 1004: Max Consecutive Ones III
"""
