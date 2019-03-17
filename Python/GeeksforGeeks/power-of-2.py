"""
Problem Link: https://practice.geeksforgeeks.org/problems/power-of-2/0

Given a positive integer N. The task is to check if N is a power of 2. That is N is 2x for some x.

Input:
The first line contains T denoting the number of test cases. Each test case contains a single positive integer N.

Output:
Print "YES" if it is a power of 2 else "NO" (Without the double quotes).

Constraints:
1 <= T <= 100
0 <= N <= 1018

Example:
Input :
2
1
98

Output :
YES
NO

Explanation:
Testcase 1:  1 is equal to 2 raised to 0 (2^0 == 1).
"""
def isPower(n):
    if not n:
        return False
    return not(n & (n-1))
for _ in range(int(input())):
    n = int(input())
    print("YES" if isPower(n) else "NO")