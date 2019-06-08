"""
Problem Link: https://practice.geeksforgeeks.org/problems/print-elements-of-array/0

Given an array, print all its elements.

Input:
The first line of the input contains T denoting the total number of testcases. The first line of each testcase contains N 
denoting the size of array. The second line contains N space separated positive integers denoting the elements of array.

Output:
For each testcase, print all its element in new line.

Constraints:
1<=T<=20
1<=N<=100
1<=a[i]<=100

Example:
Input:
1
5
1 2 3 4 5

Output:
1 2 3 4 5
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(*arr)