"""
Problem Link: https://practice.geeksforgeeks.org/problems/print-the-kth-digit/0

Given two numbers A and B, find Kth digit from right of AB.

Input:
The first line of the input contains T denoting the number of test cases. T testcases follow. 
Each of the next T lines contains three space separated positive integers denoting the value of a , b and k respectively.

Output:
For each test case, in a new line, output the Kth digit from right of AB in new line.

Constraints:
1 <= T <= 100
1 <= A , B <=15
1 <= K <= |totaldigits in AB|

Example:
Input:
2
3 3 1
5 2 2
Output:
7
2
"""
for _ in range(int(input())):
    a,b,k = map(int,input().split())
    p = a ** b
    count = 0
    while p and count < k:
        count += 1
        rem = p % 10
        p //= 10
        if count == k:
            print(rem)