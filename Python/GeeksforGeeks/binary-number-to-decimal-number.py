"""
Problem Link: https://practice.geeksforgeeks.org/problems/binary-number-to-decimal-number/0

Given a Binary Number B, Print its decimal equivalent.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follow. 
Each test case contains a single Binary number B. 

Output: 
For each testcase, in a new line, print each Decimal number in new line.

Constraints:
1 <= T <= 100
1 <= Digits in Binary <= 16

Example:
Input:
2
10001000
101100

Output:
136
44
"""
for _ in range(int(input())):
    n = int(input())
    res = count = 0
    while n:
        res += (n%10) * 2**count
        count += 1
        n //= 10
    print(res)