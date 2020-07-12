"""
Problem Link: https://www.interviewbit.com/problems/palindrome-integer/

Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with 
its digit reversed.

Negative numbers are not palindromic.

Example :
Input : 12121
Output : True

Input : 123
Output : False
"""
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, x):
        if x < 0  or (x % 10 == 0 and x != 0):
            return 0
        rev = 0
        while x > rev:
            rev = (rev*10) + (x%10)
            x //= 10
        return int(rev == x or rev//10 == x)
