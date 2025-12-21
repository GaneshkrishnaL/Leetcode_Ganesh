"""  
LeetCode Problem 2390: Removing Stars From a String

Problem Description:
-----------------
You are given a string s, which contains stars *.
In one operation, you can:
- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:
- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

Example:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation:
- Remove 't' and first '*' -> "lee*cod*e"
- Remove 'e' and second '*' -> "lecod*e"  
- Remove 'd' and third '*' -> "lecoe"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters and stars *
- The operation can always be performed

Time Complexity: O(n) where n is the length of string
Space Complexity: O(n) for the stack
"""

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Solves the problem using a stack-based approach.
        
        Approach:
        --------
        - Use a stack (list) to simulate the removal process
        - Iterate through each character in the string
        - If character is NOT a star, push it onto the stack
        - If character IS a star, pop from stack (removes previous character)
        - Join the stack at the end to form the final string
        
        Why this works:
        --------------
        - Stack naturally gives us LIFO (Last In First Out) behavior
        - When we see a '*', we need to remove the most recent non-star character
        - This is exactly what stack.pop() does
        - No need to actually modify the original string
        
        Args:
            s (str): Input string containing lowercase letters and stars
            
        Returns:
            str: Resulting string after all star removals
        """
        
        # Initialize empty stack to build our result
        # This will store characters that haven't been removed yet
        stack = []  
        
        # Process each character in the input string
        for char in s:
            # If we encounter a star, remove the last added character
            if char == '*':
                # pop() removes and returns the last element
                # The problem guarantees there's always a character to remove
                stack.pop()
            else:
                # For regular characters, add them to our result stack
                # We might remove them later if we see a star
                stack.append(char)
        
        # Convert the stack (list) back to a string
        # ''.join() concatenates all characters without any separator
        return ''.join(stack)
