class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node):
            visited.add(node) 
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for node in range(n):
            if node not in visited:
                count += 1
            dfs(node)
        return count