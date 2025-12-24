from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Determines which party (Radiant or Dire) wins in the Dota2 Senate voting process.
        
        Problem: Each senator can ban the next senator from the opposing party in a circular manner.
        The party with remaining senators wins.
        
        Approach: Greedy strategy using two queues
        - Each senator will ban the closest opposing senator (greedy choice)
        - Use queues to maintain the order of senators
        - Store indices to track voting order in the circular senate
        
        Time Complexity: O(n) where n is the length of senate string
        Space Complexity: O(n) for the two queues
        
        Args:
            senate: String containing 'R' (Radiant) and 'D' (Dire) senators
            
        Returns:
            "Radiant" if Radiant party wins, "Dire" if Dire party wins
        """
        
        # Initialize two queues to store indices of Radiant and Dire senators
        # Using deque for efficient O(1) popleft() and append() operations
        rr = deque()  # Queue for Radiant senators
        dd = deque()  # Queue for Dire senators
        
        # Populate the queues with senator indices based on their initial positions
        # Indices help us maintain the circular voting order
        for i in range(len(senate)):
            if senate[i] == "R":
                rr.append(i)
            else:  # senate[i] == "D"
                dd.append(i)
        
        # Process voting rounds until one party has no senators left
        while rr and dd:
            # Get the next senator from each party (first in queue votes first)
            r = rr.popleft()  # Next Radiant senator's index
            d = dd.popleft()  # Next Dire senator's index
            
            # Greedy strategy: The senator with smaller index votes first
            # and bans the opposing senator
            if r < d:
                # Radiant senator votes first, bans the Dire senator
                # Add Radiant back to queue with updated index (r + len(senate))
                # to represent their position in the next round of voting
                rr.append(r + len(senate))
            else:
                # Dire senator votes first, bans the Radiant senator
                # Add Dire back to queue with updated index (d + len(senate))
                # to represent their position in the next round of voting
                dd.append(d + len(senate))
        
        # The party with remaining senators wins
        return "Radiant" if rr else "Dire"
