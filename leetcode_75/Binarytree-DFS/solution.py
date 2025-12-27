from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> bool:
        """
        Compare whether two binary trees have the same leaf value sequence.

        A leaf value sequence is the sequence of values in the order you encounter
        leaf nodes during a depth-first traversal (left to right).

        Example:
            Tree 1:
                3
               / \
              5   1
            Leaves: [6,7,4,9,8]

            Tree 2:
                3
               / \
              5   1
            Leaves: [6,7,4,9,8]

            leafSimilar(tree1, tree2) returns True because the leaf sequences match.
        """
        # Helper function to collect leaf node values using DFS.
        def get_leaves(node: Optional['TreeNode'], leaves: List[int]) -> None:
            """
            Perform a depth-first search and append leaf node values to the list.

            Args:
                node: current TreeNode
                leaves: list to append leaf values
            """
            if not node:
                # Nothing to do if the node is None
                return
            if not node.left and not node.right:
                # If the node has no children, it's a leaf; record its value
                leaves.append(node.val)
                return
            # Recurse on left and right children
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        # Collect leaves for both trees
        leaves1: List[int] = []
        leaves2: List[int] = []
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)

        # Compare the two leaf sequences
        return leaves1 == leaves2
