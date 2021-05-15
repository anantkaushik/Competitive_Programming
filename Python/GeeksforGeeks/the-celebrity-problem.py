"""
Problem Link: https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1#

A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, 
find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  
is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.

Example 1:
Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:
Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and 
its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
2 <= N <= 3000
0 <= M[][] <= 1
"""
class Solution:
    
    def celebrity(self, M, n):
        
        start, end = 0, n-1
        
        while start < end:
            if self.knows(start, end, M):
                start += 1
            else:
                end -= 1
        
        celeb = start
        for person in range(n):
            if person != celeb:
                if not (self.knows(person, celeb, M) and not self.knows(celeb, person, M)):
                    return -1
        
        return celeb
    
    def knows(self, p1, p2, M):
        return M[p1][p2]
    
class Solution1:
    
    def celebrity(self, M, n):
        
        celeberities = []
        
        for i in range(n):
            num_of_known = 0
            for j in range(n):
                num_of_known += M[i][j]
            
            if not num_of_known:
                celeberities.append(i)
        
        for j in celeberities:
            num_of_known = n-1
            for i in range(n):
                num_of_known -= M[i][j]
            
            if not num_of_known:
                return j
                
        return -1