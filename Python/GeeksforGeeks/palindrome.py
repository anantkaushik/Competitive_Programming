"""
Problem Link: https://practice.geeksforgeeks.org/problems/palindrome/0

Given an integer, check whether it is a palindrome or not.

Input:
The first line of input contains an integer T denoting the number of test cases. 
For each test case there will be single line containing single integer N.

Output:
Print "Yes" or "No" (without quotes) depending on whether the number is palindrome or not.

Constraints:
1 <= T <= 1000
1 <= N <= 10000

Example:
Input:
3
6
167
55555

Output:
Yes
No
Yes
"""
for _ in range(int(input())):
    n = int(input())
    temp = n
    rev = 0
    while temp:
        rev = (rev*10)+(temp%10)
        temp //= 10
    print("Yes" if rev == n else "No")