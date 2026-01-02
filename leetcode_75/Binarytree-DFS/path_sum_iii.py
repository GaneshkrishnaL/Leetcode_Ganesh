from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        """
        Initialize a binary tree node with a value and optional left and right children.

        Args:
            val: The integer value stored in the node.
            left: Reference to the left child TreeNode.
            right: Reference to the right child TreeNode.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Count the number of paths in the binary tree where the sum of the values along
        the path equals the given targetSum. Paths can start and end at any nodes
        in the tree but must follow parent-child connections going downwards.

        This method uses a prefix sum approach with depth-first search (DFS). A
        dictionary (prefix_counts) keeps track of how many times a particular
        running sum has been seen so far on the path from the root to the current node.
        By checking if (current_sum - targetSum) exists in this dictionary, we can
        determine how many paths ending at the current node sum to targetSum.

        Example Walkthrough:
            Consider the tree:

                   10
                  /  \
                 5   -3
                / \    \
               3   2    11
              / \   \
             3  -2   1

            With targetSum = 8, the valid paths that sum to 8 are:
              1. 5 -> 3 (5 + 3 = 8)
              2. 5 -> 2 -> 1 (5 + 2 + 1 = 8)
              3. -3 -> 11 (-3 + 11 = 8)

            The function should return 3 for this tree.

        Args:
            root: The root node of the binary tree.
            targetSum: The integer sum to find along downward paths.

        Returns:
            The number of distinct paths where the sum of the node values equals targetSum.
        """
        # Counter to store the total number of valid paths found.
        self.paths = 0

        # Dictionary to store counts of prefix sums encountered.
        # Initialize with {0: 1} to account for a path that starts at the root.
        prefix_counts = {0: 1}

        def dfs(node: Optional[TreeNode], current_sum: int) -> None:
            """
            Perform a DFS traversal, updating prefix sum counts and counting valid paths.

            Args:
                node: The current TreeNode being visited.
                current_sum: The cumulative sum from the root to this node.
            """
            if not node:
                return

            # Update the running sum with the current node's value.
            current_sum += node.val

            # If there exists a prefix such that current_sum - prefix = targetSum,
            # then there is a path ending at this node summing to targetSum.
            self.paths += prefix_counts.get(current_sum - targetSum, 0)

            # Record the current running sum in the prefix_counts dictionary.
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

            # Recursively search the left and right subtrees.
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # After exploring both subtrees, decrement the count of the current_sum.
            # This backtracking step ensures that the prefix sum counts reflect the
            # current path (i.e., paths in other branches should not be affected).
            prefix_counts[current_sum] -= 1

        # Start DFS traversal from the root with an initial running sum of 0.
        dfs(root, 0)

        return self.paths
        
        
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths=0
        self.pathdict={0:1}
        def dfs(root,curr):
            if root is None:
                return None
            curr+=root.val

            self.paths+=self.pathdict.get(curr-targetSum,0)
            self.pathdict[curr]=self.pathdict.get(curr,0)+1

            if root.left:
                dfs(root.left,curr)
            if root.right:
                dfs(root.right,curr)
            self.pathdict[curr]=self.pathdict.get(curr,0)-1

        dfs(root,0)

        return self.paths



            
        
        
        
