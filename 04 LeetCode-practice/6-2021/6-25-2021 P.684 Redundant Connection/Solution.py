"""
Day 4   6/25/2021-Friday
Problem: https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one
additional edge added. The added edge has two different vertices chosen from 1 to n, and was not
an edge that already existed. The graph is represented as an array edges of length n where
edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are
multiple answers, return the answer that occurs last in the input.
"""

# Hard for a ME student...
# Below is solution given by LeetCode

import collections


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(set)

        # depth-first search
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantConnection_2(self, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            to_search = [source]
            searched = set()
            while to_search:
                curr_search = to_search.pop(0)
                searched.add(curr_search)
                for node in graph[curr_search]:
                    if node == target:
                        return True
                    elif node not in searched:
                        to_search.append(node)
            return False

        for u, v in edges:
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)


if __name__ == '__main__':
    test = Solution()
    edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
    print(test.findRedundantConnection(edges))
    print(test.findRedundantConnection_2(edges))
