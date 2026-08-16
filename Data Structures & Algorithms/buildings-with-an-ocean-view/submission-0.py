class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        mx = 0
        output = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > mx:
                output.append(i)
                mx = heights[i]
        output.reverse()
        return output