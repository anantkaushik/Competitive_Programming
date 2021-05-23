"""
Problem Link: https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].
Matrix [r+1] [c]
Matrix [r+1] [c-1]
Matrix [r+1] [c+1]
Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Example 1:
Input: N = 2
Matrix = {{348, 391},
          {618, 193}}
Output: 1009
Explaination: The best path is 391 -> 618. 
It gives the sum = 1009.

Example 2:
Input: N = 2
Matrix = {{2, 2},
          {2, 2}}
Output: 4
Explaination: No matter which path is 
chosen, the output is 4.

Your Task:
You do not need to read input or print anything. Your task is to complete the function maximumPath() which takes the size N 
and the Matrix as input parameters and returns the highest maximum path sum.

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)

Constraints:
1 ≤ N ≤ 100
1 ≤ Matrix[i][j] ≤ 1000
"""
class Solution:
    def maximumPath(self, N, Matrix):
        dp = [[0] * N for _ in range(N)]
        
        directions = [[1, 1], [1, -1], [1, 0]]
        
        max_path_sum = 0
        
        for row in range(N-1, -1, -1):
            for col in range(N):
                max_val = 0
                for r, c in directions:
                    new_row = r + row
                    new_col = c + col 
                    if new_row >= 0 and new_col >= 0 and new_row < N and new_col < N:
                        max_val = max(max_val, dp[new_row][new_col])
                
                dp[row][col] = Matrix[row][col] + max_val
                max_path_sum = max(max_path_sum, dp[row][col])
        
        return max_path_sum
