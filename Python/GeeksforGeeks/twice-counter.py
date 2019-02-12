"""
Problem Link: https://practice.geeksforgeeks.org/problems/twice-counter/0

Given an array of n words. Some words are repeated twice, we need count such words.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains an integer n denoting the number of words in the string. 
The next line contains n space separated words forming the string.

Output:
Print the count of the words which are repeated twice in the string.

Constraints:
1<=T<=105  
1<=no of words<=105
1<=length of each word<=105

Example:
Input:
2
10
hate love peace love peace hate love peace love peace
8
Tom Jerry Thomas Tom Jerry Courage Tom Courage

Output:
1
2
"""
for _ in range(int(input())):
    n = int(input())
    s = list(map(str,input().split()))
    count = 0
    d = {}
    for i in s:
        d[i] = d.get(i,0) + 1
        if d[i] == 2:
            count += 1
        if d[i] == 3:
            count -= 1 
    print(count)