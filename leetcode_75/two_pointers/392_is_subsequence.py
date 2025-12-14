"""
LeetCode 392: Is Subsequence

This module provides a solution to the LeetCode problem "Is Subsequence".
Given two strings s and t, the goal is to determine whether s is a subsequence
of t. A subsequence is obtained by deleting zero or more characters from t
without changing the order of the remaining characters.

The implemented solution uses a simple two-pointer approach that runs in
linear time relative to the length of t and constant extra space.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Check if string s is a subsequence of string t.

        Args:
            s: The candidate subsequence.
            t: The string to search within.

        Returns:
            True if s is a subsequence of t, otherwise False.

        The function iterates through the characters of t while keeping
        track of the position in s that we are trying to match. Whenever
        a matching character is found, the pointer in s is advanced. If
        the pointer reaches the end of s, it means all characters in s
        have been matched in order.

        Time Complexity:
            O(len(t)) – we examine each character of t at most once.
        Space Complexity:
            O(1) – only a few variables are used regardless of input size.
        """
        # Pointer to track the current character in s that needs to be matched.
        i = 0

        # Iterate through each character in the string t.
        for ch in t:
            # If we have already matched all characters in s, we can exit early.
            if i == len(s):
                break

            # If the current character in t matches the current character in s,
            # move the pointer in s to the next character.
            if i < len(s) and s[i] == ch:
                i += 1

        # After processing, if i equals the length of s, all characters were matched.
        return i == len(s)
