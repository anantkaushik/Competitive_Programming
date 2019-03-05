"""
Problem Link: https://www.hackerearth.com/problem/golf/string-rotator/

Given a number x and a sentence, print the sentence rotated x times clockwise if x is positive
and anti-clockwise otherwise.
Note:The sentence contains no white spaces

SAMPLE INPUT 
5
Softathlon

SAMPLE OUTPUT 
thlonSofta
"""
n = int(input())
s = input()
n = len(s) - n if n > 0 else abs(n)
print(s[n:]+s[:n])