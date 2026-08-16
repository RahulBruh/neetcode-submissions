# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        bruh = deque([root])
        size = 1
        output = []

        cur = [root.val]
        while bruh:
            node = bruh.popleft()
            if len(cur) == size:
                output.append(cur)
                cur = []
                size *= 2
            if node.left:
                bruh.append(node.left)
                cur.append(node.left.val)
            else:
                size -= 1
            if node.right:
                bruh.append(node.right)
                cur.append(node.right.val)
            else:
                size -= 1
        return output
