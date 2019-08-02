"""
Problem Link: https://practice.geeksforgeeks.org/problems/compete-the-skills/0

A and B are good friend and programmers. They are always in a healthy competition with each other. They decide to judge the best 
among them by competing. They do so by comparing their three skills as per their values. Please help them doing so as they are busy.
Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]
Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1

Input : 
The first line of input contains an integer T denoting the test cases. For each test case there will be two lines. 
The first line contains the skills of A and the second line contains the skills of B

Output : 
For each test case in a new line print the score of A and B separated by space.

Constraints :
1 ≤ T ≤ 50
1 ≤ a[i] ≤ 1017
1 ≤ b[i] ≤ 1017

Example:
Input : 
2
4 2 7
5 6 3
4 2 7
5 2 8

Output : 
1 2
0 2
"""
for _ in range(int(input())):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    resA = resB = 0
    for i in range(3):
        if a[i] > b[i]:
            resA += 1
        elif a[i] < b[i]:
            resB += 1
    print(resA,resB)