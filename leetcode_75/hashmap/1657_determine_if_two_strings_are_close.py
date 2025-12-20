"""
LeetCode Problem 1657: Determine if Two Strings Are Close
Difficulty: Medium

Problem Statement:
Two strings are considered close if you can attain one from the other using the following operations:
    - Operation 1: Swap any two existing characters.
    - Operation 2: Transform every occurrence of one existing character into another existing 
                   character, and do the same with the other character.

You can use the operations on either string as many times as necessary.

Approach:
To determine if two strings are close, we need to check two key conditions:
    1. Both strings must contain the same set of unique characters (character set equality)
    2. Both strings must have the same frequency distribution (frequency multiset equality)

Algorithm:
    1. Check if lengths are equal - if not, strings cannot be close
    2. Build frequency maps (hashmaps) for both strings
    3. Verify that both strings have the same set of characters (keys match)
    4. Verify that both strings have the same multiset of frequencies (sorted values match)

Time Complexity: O(n + k log k) where n is the length of strings and k is distinct characters
                 Since k ≤ 26 for lowercase English letters, this simplifies to O(n)

Space Complexity: O(k) where k is the number of distinct characters
                  Since k ≤ 26, this is effectively O(1)

Example Test Cases:
    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: Operation 1: swap 'a' and 'b' -> "bac", then swap 'a' and 'c' -> "bca"
    
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: Both have same chars {a,b,c} and same freq distribution [1,2,3]
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Initialize two hashmaps (dictionaries) to store character frequencies
        hashmap1 = {}  # Frequency map for word1
        hashmap2 = {}  # Frequency map for word2
        
        # Early exit: If lengths differ, strings cannot be close
        # This is because no operations can change the length of a string
        if len(word1) != len(word2):
            return False
        
        # Build frequency map for word1
        # Iterate through each character and count occurrences
        for i in word1:
            # get(i, 0) returns the current count or 0 if character not seen yet
            hashmap1[i] = hashmap1.get(i, 0) + 1
        
        # Build frequency map for word2
        # Same process as above for the second string
        for j in word2:
            hashmap2[j] = hashmap2.get(j, 0) + 1
        
        # Condition 1: Check if both strings have the same set of characters
        # Convert dictionary keys to sets and compare
        # If character sets don't match, strings cannot be close
        # Example: "abc" has {a,b,c} but "abd" has {a,b,d} - cannot be close
        if set(hashmap1.keys()) != set(hashmap2.keys()):
            return False
        
        # Condition 2: Check if both strings have the same frequency distribution
        # Sort the frequency values and compare
        # Example: word1 has frequencies [1,2,3] and word2 has [1,2,3] (when sorted)
        # This ensures we can transform one string into another using the operations
        return sorted(hashmap1.values()) == sorted(hashmap2.values())


# Alternative solution using Counter from collections module:
# from collections import Counter
# 
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False
#         
#         c1 = Counter(word1)
#         c2 = Counter(word2)
#         
#         return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
