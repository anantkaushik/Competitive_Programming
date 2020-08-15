"""
Problem Link: https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:
Input : k = 3
Return : [1,3,3,1]

NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        A += 1
        res = [0] * A
        res[0] = 1
        for i in range(1, A):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res
