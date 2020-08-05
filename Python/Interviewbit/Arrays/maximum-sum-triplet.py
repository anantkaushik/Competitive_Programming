"""
Problem Link: https://www.interviewbit.com/problems/maximum-sum-triplet/

Problem Description

Given an array A containing N integers.
You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and 
Ai < Aj < Ak.
If no such triplet exist return 0.

Problem Constraints
3 <= N <= 105.
1 <= A[i] <= 108.

Input Format
First argument is an integer array A.

Output Format
Return a single integer denoting the maximum sum of triplet as described in the question.

Example Input
Input 1:
A = [2, 5, 3, 1, 4, 9]

Input 2:
A = [1, 2, 3]

Example Output
Output 1:
16

Output 2:
6

Example Explanation
Explanation 1:
All possible triplets are:-
2 3 4 => sum = 9
2 5 9 => sum = 16
2 3 9 => sum = 14
3 4 9 => sum = 16
1 4 9 => sum = 14
Maximum sum = 16
Explanation 2:

All possible triplets are:-
1 2 3 => sum = 6
Maximum sum = 6
"""
from bisect import bisect_left 
def BinarySearch(a, x): 
    i = bisect_left(a, x)  
    return i-1 if i else -1
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_values_right = [0] * len(A) 
        max_values_right[-1] = A[-1]
        for i in range(len(A)-2, -1, -1):
            max_values_right[i] =  max(A[i], max_values_right[i+1])
        
        lst = []
        res = 0
        lst.append(A[0])
        for i in range(1,len(A)-1):
            val = BinarySearch(lst, A[i])
            if val != -1 and max_values_right[i+1] > A[i]:
                res = max(res, lst[val] + A[i] + max_values_right[i+1])
            lst.insert(val+1,A[i])
        return res
