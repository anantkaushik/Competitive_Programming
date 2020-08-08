"""
Problem Link: https://www.interviewbit.com/problems/balance-array/

Problem Description
Given an integer array A of size N. You need to count the number of special elements in the given array.
A element is special if removal of that element make the array balanced.
Array will be balanced if sum of even index element equal to sum of odd index element.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the count of special elements.

Example Input
Input 1:
A = [2, 1, 6, 4]
Input 2:
A = [5, 5, 2, 5, 8]

Example Output
Output 1:
1

Output 2:
2

Example Explanation
Explanation 1:
After deleting 1 from array : {2,6,4}
(2+4) = (6)
Hence 1 is the only special element, so count is 1

Explanation 2:
If we delete A[0] or A[1] , array will be balanced
(5+5) = (2+8)
So A[0] and A[1] are special elements, so count is 2.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        right_even = right_odd = 0
        for i in range(len(A)):
            if i % 2 == 0:
                right_odd += A[i]
            else:
                right_even += A[i]
        
        res = left_odd = left_even = 0
        for i in range(len(A)):
            if i % 2 == 0:
                right_odd -= A[i]
            else:
                right_even -= A[i]
                
            if right_odd + left_even == left_odd + right_even:
                res += 1
                
            if i % 2 == 0:
                left_odd += A[i]
            else:
                left_even += A[i]

        return res
