class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):

        # -------------------------
        # 1. Build the Trie
        # -------------------------
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            # Store the complete word at the ending node
            node.word = word

        result = []
        rows = len(board)
        cols = len(board[0])

        # -------------------------
        # 2. DFS
        # -------------------------
        def dfs(r, c, node):

            ch = board[r][c]

            # Character doesn't continue any word in Trie
            if ch not in node.children:
                return

            node = node.children[ch]

            # We found a complete word
            if node.word is not None:
                result.append(node.word)

                # Prevent duplicate results
                node.word = None

            # Mark current cell as visited
            board[r][c] = '#'

            # Four possible directions
            directions = [
                (1, 0),    # down
                (-1, 0),   # up
                (0, 1),    # right
                (0, -1)    # left
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:

                    # Don't visit an already visited cell
                    if board[nr][nc] != '#':
                        dfs(nr, nc, node)

            # Restore the cell
            board[r][c] = ch

        # -------------------------
        # 3. Start DFS from every cell
        # -------------------------
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result