class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursively get max gain from left/right subtrees.
            # Clamp negative gains to 0 -- we'd rather not include
            # a branch than let it drag the sum down.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Best path if this node is the "peak" (can use both branches)
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)

            # What we can actually return to the parent:
            # this node plus AT MOST ONE branch (can't fork upward)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum