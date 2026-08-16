# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, cuh):
            if node.val != cuh.val:
                return False
            
            if node.left and cuh.left:
                return dfs(node.left, cuh.left)
            
            elif not node.left and not cuh.left:
                pass
            
            else:
                return False

            if node.right and cuh.right:
                return dfs(node.right, cuh.right)
            
            elif not node.right and not cuh.right:
                pass

            else:
                return False

            return True
        
        if not p and not q:
            return True
        
        return dfs(p, q) if p and q else False
