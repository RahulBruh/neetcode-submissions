class Solution:
    def maxArea(self, heights: List[int]) -> int:    
        l = 0
        r = len(heights) - 1
        output = 0
        width = len(heights) - 1
        while l < r:

            if min(heights[l], heights[r]) * width > output:
                output = min(heights[l], heights[r]) * width

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

            width -= 1


        return output