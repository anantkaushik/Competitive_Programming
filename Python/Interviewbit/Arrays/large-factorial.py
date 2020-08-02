"""
Problem Link: https://www.interviewbit.com/problems/large-factorial/

Problem Description
Given a number A. Find the fatorial of the number.

Problem Constraints
1 <= A <= 100

Input Format
First and only argument is the integer A.

Output Format
Return a string, the factorial of A.


Example Input
Input 1:
A = 2

Input 2:
A = 3

Example Output
Output 1:
2

Output 2:
6

Example Explanation
Explanation 1:
2! = 2 .

Explanation 2:
3! = 6 .
"""
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        res = 1
        for num in range(2, A+1):
            res *= num
        return str(res)
