class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        output = 0
        def dfs(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == "0" or (r, c) in seen:
                return
            
            seen.add((r,c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in seen:
                    pass
                elif grid[r][c] == "1":
                    dfs(r,c)
                    output += 1
        return output