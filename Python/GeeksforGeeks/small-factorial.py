"""
Problem Link: https://practice.geeksforgeeks.org/problems/small-factorial/0

Calculate factorial of a given number N.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, it contains an integer 'N'.

Output:
In each seperate line output the answer to the problem.

Constraints:
1 <= T <= 100
1 <= N <= 18

Example:
Input :
1
5

Output:
120
"""
def fact(n):
    if n == 1: return 1
    return n * fact(n-1)
    
for _ in range(int(input())):
    print(fact(int(input())))