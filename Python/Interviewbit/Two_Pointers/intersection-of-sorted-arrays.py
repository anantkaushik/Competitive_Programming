"""
Problem Link: https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :
Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]
Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]
Output : [3 5]

NOTE : For the purpose of this problem ( as also conveyed by the sample case ), 
assume that elements that appear more than once in both arrays should be included 
multiple times in the final output. 
"""
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        res = []
        index1 = index2 = 0
        while index1 < len(A) and index2 < len(B):
            if A[index1] == B[index2]:
                res.append(A[index1])
                index1 += 1
                index2 += 1
            elif A[index1] > B[index2]:
                index2 += 1
            else:
                index1 += 1
        return res
