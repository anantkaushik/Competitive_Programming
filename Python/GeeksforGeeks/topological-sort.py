"""
Problem Link: https://practice.geeksforgeeks.org/problems/topological-sort/1/

Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  
which takes the integer V denoting the number of vertices and adjacency list as input parameters and 
returns an array consisting of a the vertices in Topological order. As there are multiple 
Topological orders possible, you may return any of them. If your returned topo sort is correct 
then console output will be 1 else 0.
"""
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited = set()
        res = []
        for v in range(V):
            self.topologicalSort(v, adj, visited, res)
        return res[::-1]
    
    def topologicalSort(self, node, adj, visited, res):
        if node in visited:
            return 
        
        visited.add(node)
        for neighbour in adj[node]:
            self.topologicalSort(neighbour, adj, visited, res)
        
        res.append(node)
