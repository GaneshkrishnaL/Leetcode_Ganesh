# File: keys_and_rooms.py  
# Description: Implementation of the Keys and Rooms problem using Depth-First Search (DFS).  
#  
# Problem:  
# There are n rooms labeled from 0 to n-1, and each room contains keys to other rooms.  
# Starting from room 0, your goal is to determine whether you can visit all rooms using the keys found along the way.  
#  
# Approach:  
# We perform a Depth-First Search starting from room 0. We use a stack to keep track of rooms to visit and a set to record visited rooms.  
# For each room we visit, we add all unvisited rooms accessible via keys to the stack.  
# At the end of the search, if the number of visited rooms equals the total number of rooms, we return True; otherwise, False.  
#  
# Walkthrough Example 1:  
# rooms = [[1], [2], [3], []]  
# Explanation:  
# - Start in room 0 and take key 1.  
# - Visit room 1 and take key 2.  
# - Visit room 2 and take key 3.  
# - Visit room 3. All rooms have been visited, so the function returns True.  
#  
# Walkthrough Example 2:  
# rooms = [[1, 3], [3, 0, 1], [2], [0]]  
# Explanation:  
# - Start in room 0 and pick up keys 1 and 3.  
# - Visit room 3 next; it contains a key to room 0, which we've already visited, so nothing new is added.  
# - Visit room 1; it contains keys to rooms 3, 0, and 1—all of which are already visited or current, so nothing new is added.  
# - Room 2 was never reached, so not all rooms can be visited. The function returns False.  
#  
# The canVisitAllRooms function below implements this logic.  

from typing import List  

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    """
    Determine if all rooms can be visited starting from room 0 using DFS.

    Args:
        rooms: A list where rooms[i] contains a list of keys for rooms accessible from room i.

    Returns:
        True if all rooms can be visited, False otherwise.
    """
    visited = set()  # set to keep track of visited rooms
    stack = [0]  # start by visiting room 0

    while stack:
        room = stack.pop()  # take the next room to visit
        if room not in visited:
            visited.add(room)  # mark the room as visited
            # add all keys (rooms) found in this room to the stack if not visited
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

    # After exploring all reachable rooms, check if we've visited every room
    return len(visited) == len(rooms)

if __name__ == "__main__":
    # Demonstrate the function with the walkthrough examples
    example_rooms = [[1], [2], [3], []]
    result1 = canVisitAllRooms(example_rooms)
    print(f"Can visit all rooms in {example_rooms}? {result1}")  
    # Expected output: True

    second_example = [[1, 3], [3, 0, 1], [2], [0]]
    result2 = canVisitAllRooms(second_example)
    print(f"Can visit all rooms in {second_example}? {result2}")  
    # Expected output: False
