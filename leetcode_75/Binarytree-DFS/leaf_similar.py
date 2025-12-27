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
        Determine if two binary trees are leaf-similar.

        Two trees are considered leaf-similar if their leaf value sequence is the same.
        The leaf value sequence is obtained by recording the values of the leaves
        from left to right.

        Args:
            root1 (Optional[TreeNode]): Root node of the first binary tree.
            root2 (Optional[TreeNode]): Root node of the second binary tree.

        Returns:
            bool: True if both trees have the same leaf value sequence, False otherwise.

        Example:
            Consider the following two trees:

                Tree 1:        3                  Tree 2:        3
                               / \                                / \
                              5   1                              5   1
                             / \   \                            /     \
                            6   2   9                          6       2
                               / \                                  \
                              7   4                                  7

            The leaf sequence for Tree 1 is [6,7,4,9], and for Tree 2 is [6,7,2].
            Since these sequences differ, the trees are not leaf-similar.

        The algorithm performs a DFS traversal to collect leaf nodes from each tree
        and compares the resulting sequences.
        """
        def dfs_collect_leaves(node: Optional['TreeNode'], leaves: List[int]) -> None:
            """Helper function to collect leaf node values via DFS."""
            if not node:
                return
            # Check if this node is a leaf (no children).
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            # Traverse left and right subtrees.
            dfs_collect_leaves(node.left, leaves)
            dfs_collect_leaves(node.right, leaves)

        leaves1: List[int] = []
        leaves2: List[int] = []

        # Collect leaves from both trees.
        dfs_collect_leaves(root1, leaves1)
        dfs_collect_leaves(root2, leaves2)

        # Compare the two leaf sequences.
        return leaves1 == leaves2
