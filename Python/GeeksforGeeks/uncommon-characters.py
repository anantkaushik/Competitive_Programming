"""
Problem Link: https://practice.geeksforgeeks.org/problems/uncommon-characters/0

Find and print the uncommon characters of the two given strings S1 and S2. Here uncommon character means that either the character 
is present in one string or it is present in other string but not in both. The strings contains only lowercase characters and 
can contain duplicates.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains 
two strings in two subsequent lines.

Output:
For each testcase, in a new line, print the uncommon characters of the two given strings in sorted order.

Constraints:
1 <= T <= 100
1 <= |S1|, |S2| <= 105

Example:
Input:
1
characters
alphabets
Output:
bclpr
"""
for _ in range(int(input())):
    alphabets = [0]*26
    s1 = input()
    s2 = input()
    for c in s1:
        alphabets[ord(c)-ord('a')] = 1
    for c in s2:
        if alphabets[ord(c)-ord('a')] == 1 or alphabets[ord(c)-ord('a')] == -1:
            alphabets[ord(c)-ord('a')] = -1
        else:
            alphabets[ord(c)-ord('a')] = 2
    
    for i in range(len(alphabets)):
        if alphabets[i] == 1 or alphabets[i] == 2:
            print(chr(i+ord('a')),end='')
    print()