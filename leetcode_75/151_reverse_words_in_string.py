"""
LeetCode Problem 151: Reverse Words in a String
Difficulty: Medium

Problem Description:
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note:
- s may contain leading or trailing spaces or multiple spaces between two words.
- The returned string should only have a single space separating the words.
- Do not include any extra spaces.

Examples:
    Input: s = "the sky is blue"
    Output: "blue is sky the"
    
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Reversed string should not contain leading or trailing spaces.
    
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: Multiple spaces between words should be reduced to a single space.

Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for storing the list of words
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a string.
        
        Approach:
        1. Use split() without arguments to split by whitespace and remove empty strings
           - This automatically handles multiple spaces, leading/trailing spaces
        2. Reverse the list of words using slicing [::-1]
        3. Join the reversed words with a single space
        
        Args:
            s (str): Input string containing words separated by spaces
            
        Returns:
            str: String with words in reverse order, single space separated
            
        Example:
            >>> solution = Solution()
            >>> solution.reverseWords("the sky is blue")
            'blue is sky the'
            >>> solution.reverseWords("  hello world  ")
            'world hello'
        """
        # split() with no arguments splits on any whitespace and removes empty strings
        # This handles multiple spaces, leading/trailing spaces automatically
        words = s.split()
        
        # Reverse the list of words using slicing and join with single space
        # [::-1] creates a reversed copy of the list
        return " ".join(words[::-1])


# Alternative Solution: More Explicit Approach
class SolutionAlternative:
    def reverseWords(self, s: str) -> str:
        """
        Alternative approach with explicit steps for educational purposes.
        
        This solution shows the step-by-step process more clearly:
        1. Strip leading/trailing whitespace
        2. Split by whitespace
        3. Filter out empty strings (from multiple spaces)
        4. Reverse the list
        5. Join with single space
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Remove leading and trailing whitespace
        trimmed = s.strip()
        
        # Split by whitespace
        words = trimmed.split()
        
        # Filter out any empty strings (though split() already does this)
        words = [word for word in words if word]
        
        # Reverse the list
        words.reverse()
        
        # Join with single space
        return " ".join(words)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic case
    test1 = "the sky is blue"
    assert solution.reverseWords(test1) == "blue is sky the", "Test 1 Failed"
    print(f"Test 1 Passed: '{test1}' -> '{solution.reverseWords(test1)}'")
    
    # Test Case 2: Leading and trailing spaces
    test2 = "  hello world  "
    assert solution.reverseWords(test2) == "world hello", "Test 2 Failed"
    print(f"Test 2 Passed: '{test2}' -> '{solution.reverseWords(test2)}'")
    
    # Test Case 3: Multiple spaces between words
    test3 = "a good   example"
    assert solution.reverseWords(test3) == "example good a", "Test 3 Failed"
    print(f"Test 3 Passed: '{test3}' -> '{solution.reverseWords(test3)}'")
    
    # Test Case 4: Single word
    test4 = "hello"
    assert solution.reverseWords(test4) == "hello", "Test 4 Failed"
    print(f"Test 4 Passed: '{test4}' -> '{solution.reverseWords(test4)}'")
    
    print("\nAll test cases passed!✓")
