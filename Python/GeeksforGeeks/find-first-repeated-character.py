"""
Problem Link: https://practice.geeksforgeeks.org/problems/find-first-repeated-character/0

Given a string S. The task is to find the first repeated character in it. We need to find the character 
that occurs more than once and whose index of first occurrence is smallest. S contains only lowercase letters.
Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. 
Each test case contains a string S.

Output:
For each test case in a new line print the first repeating character in the string. If no such character exist print -1.

Constraints:
1 <= T <= 100
1 <= |S| <=104

Example:
Input:
2
geeksforgeeks
hellogeeks

Output:
e
l
"""
def firstRepeatedChar(s):
    temp = set()
    for i in s:
        if i in temp:
            return i
        temp.add(i)
    return -1
    
for _ in range(int(input())):
    s = input()
    print(firstRepeatedChar(s))