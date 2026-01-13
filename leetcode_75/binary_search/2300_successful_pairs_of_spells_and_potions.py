from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Given arrays of spells and potions and a success threshold, return an array pairs where pairs[i] is the number of potions that will form a successful pair with the ith spell.  
        
        A spell and potion form a successful pair if spells[i] * potions[j] >= success.  
        
        This solution sorts the potions and then for each spell uses binary search to find the first potion that forms a successful pair. The count of successful potions is then the total length minus the found index.
        """
        # Sort the potions so we can binary search for the first viable potion
        potions.sort()
        pairs = []

        # Iterate through each spell
        for spell in spells:
            l = 0
            r = len(potions)
            # Binary search to find lowest index where potion * spell >= success
            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] * spell >= success:
                    # Move left to find earlier valid potion
                    r = mid
                else:
                    # Move right to search for valid potion
                    l = mid + 1
            # The number of successful potions is total potions minus left index
            pairs.append(len(potions) - l)

        return pairs
