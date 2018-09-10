"""
Problem Link: https://practice.geeksforgeeks.org/problems/binary-array-sorting/0

Given a binary array, sort it in non-decreasing order

Input: First line contains an integer denoting the test cases 'T'.  Every test case contains two lines, first line is size and 
second line is space separated elements of arra

Output:  Space separated elements of sorted arrays.  There should be a new line between output of every test case.

Input:
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0

Output:
0 0 1 1 1
0 0 0 0 1 1 1 1 1 1
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    pos = -1
    for i in range(n):
        if arr[i] == 0:
            pos+=1
            arr[i],arr[pos] = arr[pos],arr[i]
    print(*arr)