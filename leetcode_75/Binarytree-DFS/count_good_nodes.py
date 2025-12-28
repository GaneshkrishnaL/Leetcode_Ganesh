"""
LeetCode Problem 1448: Count Good Nodes in Binary Tree
Difficulty: Medium
Topic: Binary Tree - DFS (Depth-First Search)

Problem Description:
Given a binary tree root, a node X in the tree is named 'good' if in the path 
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good nodes:
- Root Node (3) is always a good node
- Node 4 -> (3,4) is the maximum value in the path starting from the root
- Node 5 -> (3,4,5) is the maximum value in the path
- Node 3 -> (3,1,3) is the maximum value in the path

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5]
- Each node's value is between [-10^4, 10^4]

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Count the number of 'good' nodes in a binary tree.
        A node is 'good' if there are no nodes with a greater value on the path from root to that node.
        
        Args:
            root: TreeNode - The root of the binary tree
            
        Returns:
            int - The count of good nodes in the tree
            
        Approach:
            - Use DFS (Depth-First Search) to traverse the tree
            - Keep track of the maximum value seen so far in the current path
            - If current node's value >= max value in path, it's a good node
            - Recursively check left and right subtrees with updated max value
        """
        
        # Initialize counter for good nodes
        # Using instance variable so it can be accessed in nested function
        self.good = 0
        
        def dfs(root, check):
            """
            Perform depth-first search to count good nodes.
            
            Args:
                root: TreeNode - Current node being examined
                check: int - Maximum value encountered in the path from tree root to current node
            
            The function updates self.good counter when a good node is found.
            """
            
            # Check if current node is a 'good' node
            # A node is good if its value is >= the maximum value seen so far in the path
            if root.val >= check:
                self.good += 1  # Increment good node counter
            
            # Explore left subtree if it exists
            if root.left:
                # Pass the maximum of current max (check) and current node's value
                # This ensures we track the highest value in the path
                dfs(root.left, max(check, root.val))
            
            # Explore right subtree if it exists
            if root.right:
                # Pass the maximum of current max (check) and current node's value
                # This ensures we track the highest value in the path
                dfs(root.right, max(check, root.val))
        
        # Start DFS from the root node
        # Initialize check with root's value since root is always a good node
        # (no nodes before it in the path)
        dfs(root, root.val)
        
        # Return the total count of good nodes found
        return self.good

"""
Algorithm Walkthrough with Example: root = [3,1,4,3,null,1,5]

Tree Structure:
        3 (root)
       / \
      1   4
     /   / \
    3   1   5

Execution trace:
1. dfs(3, 3): 3 >= 3 ✓ → good = 1
   - Go left: dfs(1, max(3,3)) = dfs(1, 3)
   - Go right: dfs(4, max(3,3)) = dfs(4, 3)

2. dfs(1, 3): 1 >= 3 ✗ → good = 1 (no change)
   - Go left: dfs(3, max(3,1)) = dfs(3, 3)

3. dfs(3, 3): 3 >= 3 ✓ → good = 2
   - No children

4. dfs(4, 3): 4 >= 3 ✓ → good = 3
   - Go left: dfs(1, max(3,4)) = dfs(1, 4)
   - Go right: dfs(5, max(3,4)) = dfs(5, 4)

5. dfs(1, 4): 1 >= 4 ✗ → good = 3 (no change)
   - No children

6. dfs(5, 4): 5 >= 4 ✓ → good = 4
   - No children

Final result: 4 good nodes (3 at root, 3 at left-left, 4 at right, 5 at right-right)


Key Insights:
1. DFS allows us to naturally track the path from root to current node
2. We only need to track the maximum value, not the entire path
3. The root node is always good (no ancestors to compare with)
4. Using max(check, root.val) ensures we pass down the largest value seen so far
5. Instance variable self.good allows the nested function to modify the counter

Common Pitfalls to Avoid:
- Don't forget to check if left/right children exist before recursing
- Remember that equality (>=) counts as a good node, not just greater than
- Make sure to pass max(check, root.val) not just root.val to children
"""}
