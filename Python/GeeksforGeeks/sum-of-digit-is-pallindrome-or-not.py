"""
Problem Link: https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not/0

Write a program to check if the sum of digits of a given number N is a palindrome number or not.

Input:
The first line of the input contains T denoting the number of testcases. T testcases follow. 
Then each of the T lines contains single positive integer N denoting the value of number.

Output:
For each testcase, in a new line, output "YES" if pallindrome else "NO". (without the quotes)

Constraints:
1 <= T <= 200
1 <= N <= 1000

Example:
Input:
2
56
98
Output:
YES
NO
"""
def addDigits(n):
    summ = 0
    while n:
        summ += n % 10
        n //= 10
    return summ
    
def isPalindrome(n):
    temp = n
    rev = 0
    while temp:
        rev = (rev * 10) + temp % 10
        temp //= 10
    return n == rev
    
for _ in range(int(input())):
    n = int(input())
    n = addDigits(n)
    print("YES" if isPalindrome(n) else "NO")