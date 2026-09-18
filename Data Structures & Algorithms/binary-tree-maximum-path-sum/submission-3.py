class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.output = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            self.output = max(self.output, node.val + leftMax + rightMax)

            return max(node.val + leftMax, node.val + rightMax)
        
        dfs(root)
        return self.output