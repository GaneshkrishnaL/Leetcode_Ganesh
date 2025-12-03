# ---------------------------------------------------------
# TIME & SPACE COMPLEXITY (Beginner Friendly Explanation)
#
# Time Complexity: O(n + m)
# We loop through both strings one character at a time.
# Each character from word1 and word2 is visited exactly once.
# Therefore, total operations = length(word1) + length(word2).
#
# Space Complexity: O(n + m)
# We build a new list called 'result' that stores all characters
# from both strings before joining them into a final string.
# The output string itself also contains all characters from both.
#
# Summary:
# ✔ Linear time (fast)
# ✔ Linear extra space (only storing final output)
# ---------------------------------------------------------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # This list will collect characters one by one
        # (Using list then join is much faster than adding to a string directly)
        result = []

        # Two pointers to move through both strings
        i = 0
        j = 0

        # Continue until we reach the end of BOTH strings
        # If one string ends earlier, the other will still continue
        while i < len(word1) or j < len(word2):
            # If word1 still has characters left, take one and move pointer
            if i < len(word1):
                result.append(word1[i])
                i += 1
            # If word2 still has characters left, take one and move pointer
            if j < len(word2):
                result.append(word2[j])
                j += 1

        # Convert list of characters into a single string
        return "".join(result)
