"""
Problem Link: https://practice.geeksforgeeks.org/problems/swap-two-numbers/0

Swap given two numbers and print them. (Try to do it without a temporary variable.)

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain two positive numbers a and b.

Output:
Print the 2 numbers after swapping.

Constraints: 
1 <= T <= 100
1 <= a <= 106
1 <= b <= 106

Example:
Input:
2
20 30
12 32

Output:
30 20
32 12
"""
for _ in range(int(input())):
    a,b = map(int,input().split())
    a,b = b,a
    print(a,b)