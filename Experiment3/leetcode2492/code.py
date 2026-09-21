class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        graph = [[] for _ in range(n + 1)]

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        visited = [False] * (n + 1)

        def dfs(node):
            visited[node] = True

            ans = float('inf')

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if not visited[nei]:
                    ans = min(ans, dfs(nei))

            return ans

        return dfs(1)
