"""
Given an array of positive integers. The task is to print the minimum product of any 
two numbers of the given array.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. First line of each 
test case contains a integer N and the second line contains N space separated array elements.

Output:
For each test case, print the minimum product of two numbers in new line.

Example:
Input:
2
4
2 7 3 4
4
5 3 6 4

Output:
6
12
"""
import heapq
t = int(input())
while t > 0:
    input()
    arr = list(map(int,input().split()))
    p = heapq.nsmallest(2, arr)
    print(p[0]*p[1])
    t -= 1