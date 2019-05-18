"""
Problem Link: https://practice.geeksforgeeks.org/problems/sum-palindrome/0

Given a number, reverse it and add it to itself unless it becomes a palindrome or number of iterations reach becom more than 5. 
If it becomes a palindrome then print that palindrome number, otherwise print -1.

Input: First line of the input contains an integer T denoting the number of test cases. Each test case has a single line containing a number.
Output: Corresponding to each test case, print the palindrome number or -1 as stated above.

Constraints:
1 <= T <= 200
1 <= N <= 1000

Example:
Input:
2
23
30
Output:
55
33
"""
def reverse(n):
    temp = n
    rev = 0
    while temp:
        rev = (rev * 10) + (temp % 10)
        temp //= 10
    return rev
    
def checkPalindrome(n):
    for _ in range(6):
        revN = reverse(n) 
        if n == revN:
            return n
        n = n + revN
    return -1
        
for _ in range(int(input())):
    print(checkPalindrome(int(input())))