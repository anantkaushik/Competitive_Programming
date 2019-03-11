"""
Problem Link: https://practice.geeksforgeeks.org/problems/closest-number/0

Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. 
If there are more than one such number, then output the one having maximum absolute value.

Input:
The first line consists of an integer T i.e number of test cases. T testcases follow.  
The first and only line of each test case contains two space separated integers N and M.

Output:
For each testcase, in a new line, print the closest number to N which is also divisible by M.

Constraints: 
1 <= T <= 100
-1000 <= N, M <= 1000

Example:
Input:
2
13 4
-15 6
Output:
12
-18
"""
def closest(a,b):
    q = int(a/b)
    p1 = b * q
    if a*b > 0:
        p2 = b * (q+1)
    else:
        p2 = b * (q-1)
    if abs(a-p1) < abs(a-p2):
        return p1
    return p2
    
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(closest(a,b))