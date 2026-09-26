# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.output = False
        def dfs(node):
            def check(node, subnode):
                if not node and not subnode:
                    return True
                elif not node or not subnode:
                    return False
                elif node.val != subnode.val:
                    return False
                
                return check(node.left, subnode.left) and check(node.right, subnode.right)
                
            if not node:
                return
            
            elif node.val == subRoot.val:
                if check(node, subRoot):
                    self.output = True
                   
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.output
        