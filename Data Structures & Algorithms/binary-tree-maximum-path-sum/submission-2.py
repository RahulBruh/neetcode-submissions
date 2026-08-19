class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            maxleft = max(dfs(node.left), 0)
            maxright = max(dfs(node.right), 0)

            price = node.val + maxleft + maxright
            if price > self.maxsum:
                self.maxsum = price
            
            return node.val + max(maxleft, maxright)
        dfs(root)
        return self.maxsum

        