"""
LeetCode 11: Container With Most Water
Difficulty: Medium
Topic: Two Pointers

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is formed between index 1 and 8.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using two pointers

Approach:
Use two pointer technique - start from both ends and move the pointer with 
smaller height inward to potentially find a larger area.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculate the maximum water that can be stored between two vertical lines.
        
        Args:
            height: List of integers representing heights of vertical lines
            
        Returns:
            int: Maximum area of water that can be contained
        """
        
        # Two key factors for maximizing water storage:
        # 1. Height of container should be large (determined by minimum of two heights)
        # 2. Width of container should be wide (distance between two lines)
        
        # Formula: Area = min(height[left], height[right]) * width
        
        # Logic: We must take the minimum of two heights because water will overflow
        # at the shorter line. The actual water level is limited by the shorter boundary.
        
        # Initialize two pointers at both ends of the array
        left = 0  # Start pointer at the beginning
        right = len(height) - 1  # End pointer at the last element
        max_area = 0  # Track the maximum area found
        
        # Continue until pointers meet
        while left < right:
            # Calculate current area
            # Width = distance between pointers
            # Height = minimum of the two heights (water level limited by shorter line)
            current_area = min(height[right], height[left]) * abs(right - left)
            
            # Update maximum area if current is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height inward
            # Rationale: The shorter line limits our water capacity
            # Moving the taller line inward would only decrease width without 
            # potential for height improvement, so we move the shorter one
            # hoping to find a taller line
            if height[left] < height[right]:
                left += 1  # Move left pointer right to find potentially taller line
            else:
                right -= 1  # Move right pointer left to find potentially taller line
        
        return max_area


# Example usage and test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Standard example
    test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Test 1: {test1}")
    print(f"Maximum water: {solution.maxArea(test1)}")  # Expected: 49
    print()
    
    # Test case 2: Simple case
    test2 = [1, 1]
    print(f"Test 2: {test2}")
    print(f"Maximum water: {solution.maxArea(test2)}")  # Expected: 1
    print()
    
    # Test case 3: Ascending heights
    test3 = [1, 2, 3, 4, 5]
    print(f"Test 3: {test3}")
    print(f"Maximum water: {solution.maxArea(test3)}")  # Expected: 6
