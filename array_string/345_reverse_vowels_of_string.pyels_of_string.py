"""
LeetCode Problem 345: Reverse Vowels of a String
Difficulty: Easy
Topic: Two Pointers, String Manipulation

Problem Description:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase).

Example 1:
    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation: The vowels in s are ['I', 'e', 'e', 'A']. After reversing, s becomes "AceCreIm".

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of printable ASCII characters

Time Complexity: O(n) - Single pass through the string
Space Complexity: O(n) - Converting string to list for in-place modifications

Author: Ganesh Krishna Lakshmisetty
Date: December 05, 2025
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Reverse only the vowels in the given string using two-pointer approach.
        
        Args:
            s (str): Input string containing printable ASCII characters
            
        Returns:
            str: String with vowels reversed
            
        Approach:
            1. Convert string to list for mutability
            2. Use two pointers (left and right) starting from both ends
            3. Move left pointer forward until a vowel is found
            4. Move right pointer backward until a vowel is found
            5. Swap the vowels at both pointers
            6. Continue until pointers meet
            7. Join list back to string and return
        """
        # Convert string to list for in-place character swapping
        s = list(s)
        
        # Get the length of the string
        length = len(s)
        
        # Define set of vowels (both uppercase and lowercase) for O(1) lookup
        vowels = set('AEIOUaeiou')
        
        # Initialize two pointers
        left = 0          # Start pointer from the beginning
        right = length - 1  # End pointer from the last character
        
        # Continue until pointers meet or cross
        while left < right:
            # Move left pointer forward until we find a vowel
            while left < right and s[left] not in vowels:
                left += 1
            
            # Move right pointer backward until we find a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap the vowels at left and right positions
            s[left], s[right] = s[right], s[left]
            
            # Move both pointers towards the center
            left += 1
            right -= 1
        
        # Join the list back to string and return
        return ''.join(s)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    test1 = "IceCreAm"
    result1 = solution.reverseVowels(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print(f"Expected: AceCreIm")
    print(f"Test 1 Passed: {result1 == 'AceCreIm'}\n")
    
    # Test Case 2
    test2 = "leetcode"
    result2 = solution.reverseVowels(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print(f"Expected: leotcede")
    print(f"Test 2 Passed: {result2 == 'leotcede'}\n")
    
    # Additional Test Case 3 - Edge case with single character
    test3 = "a"
    result3 = solution.reverseVowels(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print(f"Expected: a")
    print(f"Test 3 Passed: {result3 == 'a'}\n")
