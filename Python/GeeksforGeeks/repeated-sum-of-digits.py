"""
Problem Link: https://practice.geeksforgeeks.org/problems/repeated-sum-of-digits/0

Given an integer N, recursively sum digits of N until we get a single digit.  The process can be described below
If N < 10    
    digSum(N) = N
Else         
    digSum(N) = Sum(digSum(N))

Example:
Input : 1234
Output : 1
Explanation : The sum of 1+2+3+4 = 10, 
              digSum(x) == 10
              Hence ans will be 1+0 = 1

Input:
The first line contains an integer T, total number of test cases. Then following T lines contains an integer N.

Output:
Repeated sum of digits of N.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000000

Example:
Input
2
123
9999

Output
6
9
"""
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
    elif n % 9 == 0:
        print(9)
    else:
        print(n%9)