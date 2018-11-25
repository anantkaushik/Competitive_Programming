"""
Problem Link: https://practice.geeksforgeeks.org/problems/anagram/0

Given two strings, check whether two given strings are anagram of each other or not. An anagram of a string is another 
string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are 
anagram of each other.

Input: 
The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings 
in 'lowercase' only, in a single line.

Output:
Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 1016

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO
"""
import collections
def permutationCheck(s1,s2):
    if len(s1) != len(s2):
        return "NO"
    letters = collections.defaultdict(int)
    for i in s1:
        letters[i] += 1
    for i in s2:
        letters[i] -= 1
        if letters[i] < 0:
            return "NO"
    return "YES"
for _ in range(int(input())):
    s1,s2 = map(str,input().split())
    print(permutationCheck(s1,s2))