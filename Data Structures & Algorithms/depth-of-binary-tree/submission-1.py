# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        self.output = 0
        def dfs(node):
            if not node:
                return
            self.path += 1
            self.output = max(self.path, self.output)
            dfs(node.left)
            dfs(node.right)
            self.path -= 1
        dfs(root)
        return self.output