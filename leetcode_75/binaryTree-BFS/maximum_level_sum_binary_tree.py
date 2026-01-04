# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level=1
        roots=[root]
        max_sum=root.val
        re=1
        
        while roots!=[]:
            n=[]
            curr=0
            
            for r in roots:
                if r.left:
                    n.append(r.left)
                    curr+=r.left.val
                if r.right:
                    n.append(r.right)
                    curr+=r.right.val
            
            if n!=[] and curr>max_sum:
                max_sum=curr
                re=level+1
            
            roots=n
            level+=1
            
        return re
