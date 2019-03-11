"""
Problem Link: https://practice.geeksforgeeks.org/problems/lcm-and-gcd/0

Given two numbers A and B. The task is to find out their LCM and GCD.

Input:
The first line of input contains an integer T denoting the number of testcases. T testcases follow. 
In each test cases, there are two numbers A and B separated by space.

Output:
For each testcase in a new line, print LCM and GCD separated by space.

Constraints:
1 <= T <= 100
1 <= a <= 10
1 <= b <= 1000

Example:
Input:
2
5 10
14 8

Output:
10 5
56 2

Explanation:
Testcase 1: LCM and GCD of given numbers 5 and 10 are: 10 and 5.
"""
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

for _ in range(int(input())):
    a,b = map(int,input().split())
    gcdAB = gcd(a,b)
    lcm = (a*b)//gcdAB
    print(lcm,gcdAB)