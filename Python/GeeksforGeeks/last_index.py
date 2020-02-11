"""
Given a string S containing all the characters and a character X, the task is to find last index of X in string S.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. First line of each test case contains 
a string S and the second line contains a character X.

Output:
For each test case, print the last index in new line, If X is not present in the string print '-1'.

Example:
Input:
2
Geeks
e
Hello world
o
Output:
2
7
"""
t = int(input())
while t > 0:
    s = input()
    w = input()
    print(s.rfind(w))
    t -= 1