"""
2_gcd_of_strings.py

This Python file contains a solution to the LeetCode problem "Greatest Common Divisor of Strings" (problem #1071). The goal of the problem is to find the largest string that divides two given strings. A string X divides another string Y if Y is made by concatenating X some number of times.

The solution uses a simple check to determine if the two strings share a common base pattern and then uses the built‑in math.gcd function to find the greatest common divisor of their lengths. The substring of that length from the first string is the greatest common divisor string.

The code below is designed to be easy to understand for beginners. It includes explanatory comments and a detailed docstring describing the approach.
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the greatest common divisor (GCD) string of two strings.

        Two strings are said to have a GCD string if there exists a non-empty string X
        such that both str1 and str2 can be constructed by repeating X some number of times.

        This method works in two main steps:
        1. **Pattern check**: Concatenate str1 and str2 in both possible orders (str1 + str2 and str2 + str1).
           If the results are different, it means the strings do not share the same repeating pattern,
           and therefore there is no common divisor string. In that case, we return an empty string.
        2. **GCD of lengths**: If the pattern check passes, then we compute the greatest common divisor (GCD)
           of the lengths of str1 and str2. The prefix of str1 with length equal to this GCD will be the
           greatest common divisor string, because it will also perfectly divide str2.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            str: The largest string that divides both str1 and str2. If no such string exists, returns an empty string.

        Time Complexity:
            O(n + m), where n and m are the lengths of str1 and str2 respectively. The concatenation and comparison
            operations take O(n + m) time, and computing the GCD of two integers is very fast.

        Space Complexity:
            O(1), aside from the space used to store the result, as the algorithm operates in constant extra space.
        """
        # Step 1: Check if concatenating in different orders gives the same result.
        # If they differ, there is no common divisor string.
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Compute the greatest common divisor of the lengths of the two strings.
        gcd_length = math.gcd(len(str1), len(str2))

        # The substring of str1 from the beginning to gcd_length will also divide str2,
        # so it is the greatest common divisor string.
        return str1[:gcd_length]
