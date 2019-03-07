"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-digit/0

Write a program to reverse digits of a number N.

Input:
The first line of input contains an integer T, denoting the number of test cases. T testcases follow. 
Each test case contains an integer N.

Output:
For each test case, print the reverse digits of number N .

Constraints:
1 ≤ T ≤ 104
1 ≤ N ≤ 1015

Example:
Input:
2
200
122
Output:
2
221
"""
def rev(n):
    rev = 0
    while n:
        rev = rev*10 + (n%10)
        n //= 10
    return rev
    
for _ in range(int(input())):
    n = int(input())
    print(rev(n))