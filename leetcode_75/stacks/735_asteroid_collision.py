"""
LeetCode Problem 735: Asteroid Collision
Difficulty: Medium
Topic: Stack

Problem Description:
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example:
    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Time Complexity: O(n) where n is the number of asteroids
Space Complexity: O(n) for the stack in worst case

Approach:
We use a stack-based approach where we process each asteroid one by one.
- Positive asteroids (moving right) are always added to the stack
- Negative asteroids (moving left) need to be checked against the stack:
  * If they collide with positive asteroids, we resolve based on size
  * If no collision occurs, add to stack
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Initialize an empty list to use as a stack
        # This will store the asteroids that survive all collisions
        l = []
        
        # Iterate through each asteroid in the input array
        for i in asteroids:
            # Handle collision scenarios when:
            # 1. Stack is not empty (l is True)
            # 2. Last asteroid in stack is moving right (l[-1] > 0)
            # 3. Current asteroid is moving left (i < 0)
            # These conditions indicate a potential collision
            while l and l[-1] > 0 and i < 0:
                # Pop the last asteroid from stack to compare
                last = l.pop()
                
                # Case 1: Right-moving asteroid is larger
                # The left-moving asteroid (i) explodes, right-moving survives
                if last > -i:
                    l.append(last)  # Put the surviving asteroid back
                    break  # Current asteroid destroyed, move to next
                
                # Case 2: Both asteroids are equal in size
                # Both asteroids explode (neither added back to stack)
                if last == -i:
                    break  # Both destroyed, move to next asteroid
                
                # Case 3 (implicit): Left-moving asteroid is larger (last < -i)
                # The right-moving asteroid explodes (already popped)
                # Loop continues to check if left-moving collides with next asteroid
            
            # The else clause executes when the while loop completes without break
            # This happens when:
            # 1. Stack is empty, OR
            # 2. Last asteroid in stack is moving left (l[-1] < 0), OR
            # 3. Current asteroid is moving right (i > 0), OR
            # 4. Left-moving asteroid destroyed all right-moving ones it met
            else:
                l.append(i)  # Add current asteroid to stack
        
        # Return the final state of asteroids after all collisions
        return l
