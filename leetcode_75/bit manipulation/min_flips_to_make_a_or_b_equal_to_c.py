"""
Problem: Minimum Flips to Make a OR b Equal to c

This problem asks for the minimum number of bit flips needed so that the bitwise OR of two integers `a` and `b` equals another integer `c`. A bit flip means changing a single bit from 0 to 1 or from 1 to 0.

Approach:
- We process the integers bit by bit from the least significant bit (LSB) to the most significant bit.
- At each bit position, we examine the bits of `a`, `b`, and `c`.
  - If the bit in `c` is 0, then both corresponding bits in `a` and `b` must also be 0 to satisfy `(a | b) == c` at that position. If either `a` or `b` has a 1 in this position, we need to flip those bits to 0. The number of flips required at this bit is therefore the sum of the bits from `a` and `b` at this position (`abit + bbit`).
  - If the bit in `c` is 1, then at least one of the bits in `a` or `b` must be 1. If both bits are 0, we need to flip one of them to 1 to satisfy the OR condition. This requires exactly one flip.
- After processing the current LSB, we right-shift `a`, `b`, and `c` by one to move on to the next bit.
- We continue this process until all bits of `a`, `b`, and `c` have been processed.

This greedy bit-by-bit approach ensures that we count only the necessary flips to achieve the desired OR value at each bit position.
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """Return the minimum number of bit flips required so that (a | b) == c.

        We iterate through each bit position of a, b, and c. At each step, we determine
        if flips are needed based on the following rules:
        - If the target bit in c is 0, both corresponding bits in a and b must be 0.
          Therefore, any 1s in a or b at this position must be flipped to 0.
        - If the target bit in c is 1, at least one of the bits in a or b must be 1.
          If both bits are 0, we flip one of them to 1.

        Args:
            a (int): first integer input
            b (int): second integer input
            c (int): target integer whose bits should match the OR of a and b

        Returns:
            int: the minimum number of bit flips required
        """
        flips = 0  # initialize flip counter

        # Continue looping until all bits in a, b, and c have been processed
        while a > 0 or b > 0 or c > 0:
            # Extract the least significant bit (LSB) of each number using bitwise AND with 1
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if cbit == 0:
                # When the target bit is 0, both a and b bits must be 0.
                # Any 1 bits in a or b need to be flipped off.
                flips += abit + bbit
            else:
                # When the target bit is 1, at least one of a or b must have a 1.
                # If both bits are 0, we need exactly one flip to set one of them to 1.
                if (abit | bbit) == 0:
                    flips += 1

            # Shift bits right by one to process the next bit in the next iteration.
            a >>= 1
            b >>= 1
            c >>= 1

        return flips
