class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        cols, rows = len(board[0]), len(board)

        def dfs(r, c, cur, i): 
            if i == len(word):
                return True
            if r >= rows or r < 0 or c >= cols or c < 0 or len(cur) > len(word) or (r, c) in seen or board[r][c] != word[i]:
                return False
            prev = cur
            cur += board[r][c]
            seen.add((r,c))
            cuh = (
                dfs(r + 1, c, cur, i + 1) or
                dfs(r - 1, c, cur, i + 1) or
                dfs(r, c + 1, cur, i + 1) or 
                dfs(r, c - 1, cur, i + 1)
            )
            seen.remove((r,c))
            return cuh

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, "", 0):
                    return True
        return False