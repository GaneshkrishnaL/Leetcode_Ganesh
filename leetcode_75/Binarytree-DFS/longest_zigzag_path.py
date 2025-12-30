"""LeetCode Problem 1372: Longest ZigZag Path in a Binary Tree

Problem Description:
====================
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.

Constraints:
- The number of nodes in the tree is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Depth-First Search (DFS) with Direction Tracking
        =========================================================
        
        Key Insight:
        - At each node, we track the current direction we came from (left or right)
        - If we came from left, we should go right next to continue the zigzag
        - If we came from right, we should go left next to continue the zigzag
        - When we break the zigzag pattern, we restart with length 1
        
        Algorithm:
        1. Use a helper DFS function that tracks:
           - Current node (r)
           - Direction we came from (left: True/False)
           - Current path length (curr)
        2. At each node, update the global maximum path length
        3. If we came from left (left=True):
           - Continue zigzag: go RIGHT with curr+1
           - Restart: go LEFT with length 1
        4. If we came from right (left=False):
           - Continue zigzag: go LEFT with curr+1
           - Restart: go RIGHT with length 1
        5. Start DFS from both children of root with initial length 1
        
        Time Complexity: O(N) where N is the number of nodes
        Space Complexity: O(H) where H is the height (recursion stack)
        """
        
        # Initialize the maximum path length found so far
        self.path = 0
        
        def dfs(r, left, curr):
            """
            DFS helper function to explore zigzag paths
            
            Parameters:
            - r: current node
            - left: boolean indicating if we came from left (True) or right (False)
            - curr: current zigzag path length
            """
            # Base case: if node is None, return
            if r is None:
                return
            
            # Update the maximum path length seen so far
            self.path = max(self.path, curr)
            
            # If we came from LEFT, we should go RIGHT to continue the zigzag
            if left:
                # Continue zigzag: go to right child with incremented length
                dfs(r.right, False, curr + 1)
                # Start new zigzag: go to left child with length 1 (breaking pattern)
                dfs(r.left, True, 1)
            # If we came from RIGHT, we should go LEFT to continue the zigzag
            else:
                # Start new zigzag: go to right child with length 1 (breaking pattern)
                dfs(r.right, False, 1)
                # Continue zigzag: go to left child with incremented length
                dfs(r.left, True, curr + 1)
        
        # Start DFS from both children of root
        # Try starting with going right from root
        dfs(root.right, False, 1)  # left=False means we're going right
        # Try starting with going left from root
        dfs(root.left, True, 1)    # left=True means we're going left
        
        # Return the maximum zigzag path length found
        return self.path


"""
EXAMPLE WALKTHROUGH:
===================

Example 1: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]

Tree Structure:
        1
         \
          1
         / \
        1   1
             \
              1
             / \
            1   1
               /
              1

Step-by-step execution:

1. Start from root (val=1)
   - Call dfs(root.right, False, 1) -> node with val=1 (right child)
   - Call dfs(root.left, True, 1) -> None (no left child)

2. At node 1 (root's right child), left=False, curr=1
   - Update self.path = max(0, 1) = 1
   - Since left=False (came from right):
     * dfs(right_child, False, 1) -> restart
     * dfs(left_child, True, 1+1=2) -> continue zigzag (LEFT)

3. At node 1 (left child), left=True, curr=2
   - Update self.path = max(1, 2) = 2
   - Since left=True (came from left):
     * dfs(right_child=None, False, 2+1=3) -> continue zigzag (RIGHT)
     * dfs(left_child=None, True, 1) -> restart

4. At node 1 (right child from step 2), left=False, curr=1
   - Update self.path = max(2, 1) = 2
   - Since left=False:
     * dfs(right_child, False, 1) -> restart
     * dfs(left_child, True, 1+1=2) -> continue zigzag

5. Continue exploring... The zigzag path: RIGHT -> LEFT -> RIGHT
   This gives us a path length of 3 (the blue path in LeetCode diagram)

Final Answer: 3


Example 2: root = [1,1,1,null,1,null,null,1,1,null,1]

Tree Structure:
        1
       / \
      1   1
       \
        1
       / \
      1   1
       \
        1

The longest zigzag path is: LEFT -> RIGHT -> LEFT -> RIGHT = 4 nodes (length 4)

Final Answer: 4


Example 3: root = [1]
Only one node, no zigzag path possible.
Final Answer: 0


KEY INSIGHTS:
=============
1. We need to try starting from both left and right children of root
2. At each node, we explore both continuing the zigzag and starting fresh
3. The direction parameter helps us know which way maintains the zigzag
4. We use a global variable (self.path) to track the maximum across all paths
"""
