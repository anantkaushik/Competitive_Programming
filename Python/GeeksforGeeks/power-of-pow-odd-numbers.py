"""
Problem Link: https://practice.geeksforgeeks.org/problems/power-of-pow-odd-numbers/0

Given a single integer N, your task is to find the sum of the square of first N odd natural Numbers.

Examples:
Input : 3
Output : 35 
12 + 32 + 52 = 35

Input : 8
Output : 680
12 + 32 + 52 + 72 + 92 + 112 + 132 + 152 

Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. 
The only line of each test case contains an integer N.

Output:
For each test case output the required anser on a new line.

Input:
3
2
5
9

Output:
10
165
969
"""
for _ in range(int(input())):
    n = int(input())
    print(n*(4*n*n - 1)//3)