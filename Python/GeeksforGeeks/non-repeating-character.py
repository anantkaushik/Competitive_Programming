"""
Problem link: https://practice.geeksforgeeks.org/problems/non-repeating-character/0

Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each case begins with a single integer N denoting the length of string. The next line contains the string S.

Output:
For each testcase, print the first non repeating character present in string. 
Print -1 if there is no non repeating character.

Constraints:
1 <= T <= 900
1 <= N <= 104

Example:
Input : 
3
5  
hello
12
zxvczbtxyzvy
6
xxyyzz

Output :
h
c
-1
"""
def firstUnique(s):
    count = {}
    for i in s:
        count[i] = count.get(i,0) + 1
    index = 0
    for ch in s:
        if count[ch] == 1:
            return s[index]
        else:
            index += 1       
    return -1
    
for _ in range(int(input())):
     n = int(input())
     s = input()
     print(firstUnique(s))