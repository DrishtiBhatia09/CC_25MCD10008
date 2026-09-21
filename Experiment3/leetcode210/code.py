from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(result) == numCourses:
            return result

        return []
        
