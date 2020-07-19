"""
Problem Link: https://practice.geeksforgeeks.org/problems/anagram-palindrome/0

Given a string S, Check if characters of the given string can be rearranged to form a palindrome. 
For example characters of “geeksogeeks” can be rearranged to form a palindrome “geeksoskeeg”, but characters of 
“geeksforgeeks” cannot be rearranged to form a palindrome.

Input:
First line consists of integer T  denoting the number of test cases. T testcases follow. For each testcase there are 
one line of input containing string S.

Output:
For each testcase, in a new line, print "Yes" if is possible to make it a palindrome, else "No".

Constraints:
1 <= T <= 100
1 <= |S| <= 1000

Example:
Input:
2
geeksogeeks
geeksforgeeks
Output:
Yes
No
"""
def palindromePermutation(s):
    alphabets = set()
    for c in s:
        if c in alphabets:
            alphabets.remove(c)
        else:
            alphabets.add(c)
    return len(alphabets) <= 1
        

for _ in range(int(input())):
    print("Yes" if palindromePermutation(input()) else "No")
    