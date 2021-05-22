"""
Problem Link: https://practice.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph5311/1

Given a directed graph with V nodes and E edges. If there is an edge from u to v then u depends on v. 
Find out the sum of dependencies for every node. Duplicate edges should be counted as separate edges.

Example 1:
Input:
V=4
E=4
Edges={ {0,2},{0,3},{1,3},{2,3} }

Output:
4
Explanation:
For the graph in diagram, A depends
on C and D i.e. 2, B depends on D i.e.
1, C depends on D i.e. 1
and D depends on none.
Hence answer -> 0 + 1 + 1 + 2 = 4

Example 2:
Input:
V=4
E=3
Edges={ {0,3},{0,2},{0,1} }
Output:
3

Explanation:
The sum of dependencies=3+0+0+0=3.

Your Task:
You don't need to read input or print anything.Your task is to complete the function sumOfDependencies() 
which takes the adj (Adjacency list) and V (Number of nodes)as input parameters and returns the total sum of dependencies 
of all nodes.

Expected Time Complexity:O(V)
Expected Auxillary Space:O(1)

Constraints:
1<=V,E<=150
0<= Edges[i][0],Edges[i][1] <= V-1
"""
class Solution:
    def sumOfDependencies(self,adj,V):
        count = 0
        for edges in adj:
            count += len(edges)
        return count
