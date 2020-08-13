"""
Problem Link: https://www.interviewbit.com/problems/pascal-triangle/

Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Given numRows = 5,

Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 1:
            return [[1]]
        res = []
        for i in range(A):
            row = [1]*(i+1)
            res.append(row)
            for j in range(1,len(row)-1):
                res[i][j] = res[i-1][j-1]+res[i-1][j] 
        return res
