class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = set()
        path = set()
        result = []

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True
            
            visited.add(course)
            path.add(course)

            for next_courses in graph[course]:
                if not dfs(next_courses):
                    return False
            
            path.remove(course)
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result[::-1]