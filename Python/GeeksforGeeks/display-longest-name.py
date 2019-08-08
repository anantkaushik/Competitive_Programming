"""
Problem Link: https://practice.geeksforgeeks.org/problems/display-longest-name/0

Given a list of names, display the longest name.

Input: 
First line of input contains an integer T, the number of test cases. For each test case, there will be two lines. 
First line contains integer N i.e. total number of names, and second line contains N space seperated names of different length.

Output: 
Longest name in the list of names.

Constraints:
1 <= T <= 10
1 <= N <= 10
1 <= |length of name| <= 1000

Example:
Input:
1
5
Geek
Geeks
Geeksfor
GeeksforGeek
GeeksforGeeks

Output:
GeeksforGeeks
"""
for _ in range(int(input())):
    n = int(input())
    longest_name = ""
    name_length = 0
    for i in range(n):
        s = input()
        if len(s) > name_length:
            longest_name = s
            name_length = len(s)
    print(longest_name)