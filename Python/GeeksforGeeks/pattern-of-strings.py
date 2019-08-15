"""
Problem Link: https://practice.geeksforgeeks.org/problems/pattern-of-strings/0/?ref=self

Given a string of length N, print the pattern of strings with first line with the given 
length of string and keep printing in new line the strings in decreasing order of length 
till you print the single first character of the given string. 

Input: First line of the input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consist of only one line which contains a string of length N.

Output: Corresponding to each test case, pattern is printed in a new line.

Constraints:
1 <=T<= 30
N = 5

Example:
Input:
2
Geeks
th%ik

Output:
Geeks
Geek
Gee
Ge
G
th%ik
th%i
th%
th
t
"""
for _ in range(int(input())):
    s = input()
    l = len(s)
    for i in range(len(s)):
        print(s[:l-i])