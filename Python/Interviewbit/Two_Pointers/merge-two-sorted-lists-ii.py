"""
Problem Link: https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.

If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after 
your code is executed should be m + n

Example :
Input : 
         A : [1 5 8]
         B : [6 9]
Modified A : [1 5 6 8 9]
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        m = len(A) - 1
        n = len(B) - 1
        index = len(A) + len(B) - 1
        A += [0] * len(B)
        while m >= 0 and n >=0:
            if A[m] > B[n]:
                A[index] = A[m]
                m -= 1
            else:
                A[index] = B[n]
                n -= 1
            index -= 1
        
        while n >= 0:
            A[index] = B[n]
            n -= 1
            index -= 1
        return A
