"""
Problem Link: https://www.interviewbit.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Given s = "Hello World",
return 5 as length("World") = 5.
Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
"""
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        index = len(A) - 1
        while index >= 0 and A[index] == ' ':
            index -= 1
        
        for i in range(index, -1, -1):
            if A[i] == ' ' and flag:
                return len(A) - i - 1
        return index if index != -1 else 0
