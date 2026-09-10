class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax, rightMax = [], deque()

        high = float('-inf')

        for h in height:
            high = max(high, h)
            leftMax.append(high)
        high = float('-inf')

        for h in reversed(height):
            high = max(high, h)
            rightMax.appendleft(high)
        
        output = 0

        for h in range(1, len(height)-1):
            cur = min(leftMax[h], rightMax[h]) - height[h]
            output += cur if cur > -1 else 0
        return output

