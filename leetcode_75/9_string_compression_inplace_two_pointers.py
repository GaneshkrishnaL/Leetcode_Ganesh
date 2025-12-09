"""
9. String Compression (LeetCode 443)
LeetCode 75 – Array / String

Problem summary:
- We are given a list of characters, e.g. ["a", "a", "b", "b", "c", "c", "c"].
- We must "compress" it in-place using the following rules:
    * Consecutive repeating characters become: <char><count>
      - "aa" -> "a2"
      - "ccc" -> "c3"
    * If a character appears only once, we just keep the character (no count).
- We must modify the input list `chars` directly and return the new length.
- Characters beyond the returned length can be ignored.

Example:
    Input:  ["a","a","b","b","c","c","c"]
    Output: ["a","2","b","2","c","3"], return 6

Key constraints:
- 1 <= len(chars) <= 2000
- Only constant extra space is allowed (O(1) space).

High-level idea (two pointers):
- We will use two indexes:
    1. `i`  -> "read" pointer to scan through the array.
    2. `ix` -> "write" pointer to write the compressed form into the same array.

- We process the array in groups of consecutive equal characters.
  For each group:
    1. Count how many times the current character repeats (group length).
    2. Write the character once at position `ix`.
    3. If the group length > 1, convert the count to a string and write each digit
       (e.g., 12 -> "1", "2") into the array starting at `ix`.
    4. Move `i` to the start of the next group.
- At the end, `ix` will be the length of the compressed string and we return it.

Time complexity:
    - O(n), where n = len(chars).
    - We go through the list once, and each character is part of exactly one group.

Space complexity:
    - O(1) extra space.
    - We only use a few integer variables and do all modifications in-place.
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compresses the list of characters in-place and returns the new length.

        :param chars: List of characters representing the original string.
        :return: The length of the compressed list prefix.
        """

        # `i`  -> read pointer, points to the start of the current group
        # `ix` -> write pointer, where we write the compressed characters
        i = 0
        ix = 0

        # We continue until `i` has scanned all characters
        while i < len(chars):
            # At least one occurrence of chars[i] exists (the one at position i)
            group = 1

            # Count how many times chars[i] repeats consecutively.
            # We look ahead with `group + i` while:
            #  - it is still inside the list
            #  - the next character is the same as chars[i]
            while (group + i) < len(chars) and chars[group + i] == chars[i]:
                group += 1

            # At this point:
            # - chars[i] is the character of the current group
            # - `group` is the number of times it repeats

            # STEP 1: Write the character itself at the write position `ix`
            chars[ix] = chars[i]
            ix += 1  # We used one slot for the character

            # STEP 2: If the group size is more than 1, write the count as digits
            if group > 1:
                # Convert the integer count into a string.
                # Example: if group = 12, g = "12"
                g = str(group)

                # We need to write each digit of the count into the chars list.
                # For example, "12" becomes '1', '2' in two positions.
                # We can use slicing to assign multiple positions at once:
                # chars[ix : ix + len(g)] = list(g)
                chars[ix:ix + len(g)] = list(g)

                # Move the write pointer by the number of digits we wrote.
                ix += len(g)

            # STEP 3: Move the read pointer `i` to the start of the next group.
            # We skip over all characters we just processed in this group.
            i += group

        # When we finish the loop:
        # - The first `ix` elements of `chars` contain the compressed string.
        # - Elements from ix onward do not matter.
        return ix
