# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        # case 1: no left child -> return right subtree
        if root.left is None:
            return root.right

        # case 2: no right child -> return left subtree
        if root.right is None:
            return root.left

        # case 3: both children exist
        right = root.right
        left = root.left

        # find the largest node in left subtree (rightmost of left)
        curr = left
        while curr.right:
            curr = curr.right

        # attach original right subtree to that largest node
        curr.right = right

        # return new root (left subtree becomes replacement)
        return left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # if the root itself is the key
        if root.val == key:
            return self.helper(root)

        curr = root

        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                root = root.right

        return curr
