class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store complete word at end node

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []
        seen = set()

        def dfs(r, c, parent):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in seen:
                return

            ch = board[r][c]
            curr = parent.children.get(ch)
            if curr is None:
                return

            if curr.word is not None:
                result.append(curr.word)
                curr.word = None  # avoid duplicate additions

            seen.add((r,c))
            dfs(r+1, c, curr)
            dfs(r-1, c, curr)
            dfs(r, c+1, curr)
            dfs(r, c-1, curr)
            seen.remove((r,c))

            board[r][c] = ch  # backtrack

            # Optimization: prune leaf nodes with no children left
            if not curr.children:
                parent.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result