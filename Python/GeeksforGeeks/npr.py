"""
Problem Link: https://practice.geeksforgeeks.org/problems/npr/0

Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

Input: 
The first line of the input contains T denoting the number of testcases. T testcases follow. 
First line of the test case will be the value of n and r respectively.

Output:
For each test case, in a new line, output will be the value of nPr.

Constraints:
1 <= T <= 100
1 <= n,r <= 20
n >= r

Example:
Input:
2
2 1
10 4
Output:
2
5040
"""
for _ in range(int(input())):
    n,r = map(int,input().split())
    nPr = 1
    for i in range(n,n-r,-1):
        nPr *= i
    print(nPr)