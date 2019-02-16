"""
Problem Link: https://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy/0

Given a positive integer n, find if it can be expressed as xy where y > 1 and x > 0 and x and y both are both integers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow . 
Each test cases contains an integer N.

Output:
For each test case in a new line print 1 if the number can be expressed as  xy else print 0.

Constraints:
1<=T<=1000
1<=n<=100

Example:
Input:
2
8
5
Output:
1
0
"""
def isPower(n):
    if n == 1:
        return 1
    for i in range(2,int(n**.5)+1):
        p = i
        while p <= n:
            p *= i
            if p == n:
                return 1
    return 0
    
for _ in range(int(input())):
    n = int(input())
    print(isPower(n))