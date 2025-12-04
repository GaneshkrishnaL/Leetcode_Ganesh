# 1431. Kids With the Greatest Number of Candies
# --------------------------------------------------
# Beginner Friendly Explanation:
# We are given:
#   1) A list of integers "candies"
#   2) A number "extraCandies"
#
# For each kid, we pretend to give them ALL extra candies.
# Then we check — can this kid become one of the kids
# with the greatest number of candies?
#
# Example:
# candies = [2,3,5,1,3], extraCandies = 3
# max value = 5
# For kid with 2 candies: 2 + 3 = 5  -> >= 5  -> True
# For kid with 1 candy:   1 + 3 = 4  -> <  5  -> False
#
# Result = [True, True, True, False, True]
#
# --------------------------------------------------
# Time Complexity: O(n)  — we scan the list once
# Space Complexity: O(n) — we create a new boolean list
# --------------------------------------------------

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Step 1: Find the current highest number of candies among all kids
        greatest = max(candies)  
        
        # Step 2: Prepare a result list
        result = []
        
        # Step 3: For each kid, check if giving extraCandies 
        #         makes them equal to or greater than the current max
        for candy in candies:
            
            # If >= greatest, append True
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                # Otherwise append False
                result.append(False)
        
        # Step 4: Return final boolean list
        return result
