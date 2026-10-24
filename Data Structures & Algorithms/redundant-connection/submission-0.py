class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]
        
        def dfs(node, target):
            if node == target:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target):
                        return True
            return False
        
        for a, b in edges:
            visited = set()
            if dfs(a,b):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)