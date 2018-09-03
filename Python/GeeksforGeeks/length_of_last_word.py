"""
Given a string s consisting of upper/lower-case alphabets and empty space characters ‘ ‘, 
return length of the last word in the string. If the last word does not exist, return 0.
Note: The string can end with empty spaces also.

Input:
First line consists of T test cases. The only line of every test case consists of String S.

Output:
Single line output, Print the length of last word of string.

Input:
2
Geeks for Geeks
Start Coding Here
Output:
5
4
"""
t = int(input())
while t > 0:
    s = list(map(str,input().split()))
    l = len(s) -1
    print(len(s[l]))
    t -= 1