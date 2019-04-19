"""
A string s is called a good string if and only if two consecutive letters are not the same. For example, abcab and cda  are good 
while abaa and accba are not.
You are given a string s. Among all the good substrings of s ,print the size of the longest one.

Input format
A single line that contains a string s.

Output format
Print an integer that denotes the size of the longest good substring of s.

SAMPLE INPUT 
ab
SAMPLE OUTPUT 
2

Explanation
The complete string is good so the answer is 2.
"""
s = input()
length = maxLength = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        length = 1
    else:
        length += 1
    if maxLength < length:
        maxLength = length
print(maxLength)