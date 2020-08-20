"""
Problem Link: https://www.interviewbit.com/problems/palindrome-string/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        start, end = 0, len(A) - 1
        while start < end:
            if not A[start].isalnum():
                start += 1
            elif not A[end].isalnum():
                end -= 1
            elif A[start].lower() != A[end].lower():
                return 0
            else:
                start += 1
                end -= 1
        return 1
