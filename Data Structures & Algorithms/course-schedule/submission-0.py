class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()

        def dfs(course):

            if course in path:
                return False

            if course in visited:
                return True

            visited.add(course)
            path.add(course)

            # explore neighbors here
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # remove from path here
            path.remove(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True