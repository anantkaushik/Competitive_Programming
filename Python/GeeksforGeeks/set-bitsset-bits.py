"""
Problem Link: https://practice.geeksforgeeks.org/problems/set-bits/0

Given a positive integer N, print count of set bits in it. For example, if the given number is 6(binary: 110), 
output should be 2 as there are two set bits in it.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each testcase contains single line of input containing the N.

Output:
For each test case, in a new line, print count of set bits in it.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106

Example:
Input:
2
6
11
Output:
2
3
"""
def countSetBits(n):
    if n == 0:
        return 0
    return countSetBits(n&(n-1)) + 1
    
for _ in range(int(input())):
    print(countSetBits(int(input())))