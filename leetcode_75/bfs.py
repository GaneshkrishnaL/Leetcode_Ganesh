# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        que=[]
        start=[root]
        final=[]
        
        while start!=[] and root is not None:
            
            for node in start:
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            final.append(node.val)
            start=que
            que=[]
            
        return final
