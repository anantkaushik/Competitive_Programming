"""
Problem Link: https://practice.geeksforgeeks.org/problems/positive-and-negative-elements/0

Given an array containing equal number of positive and negative elements, arrange the array such that every 
positive element is followed by a negative element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of two lines. First line of each test case contains an Integer N denoting size of 
array and the second line contains N space separated elements.

Output:
For each test case, in a new line print the arranged array.

Constraints:
1 <= T <= 300
2 <= N <= 105
-105 <= A[i] <= 105

Example:
Input:
2
6
-1 2 -3 4 -5 6
4
-3 2 -4 1
Output:
2 -1 4 -3 6 -5
2 -3 1 -4
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    newarr = [0]*(n)
    indexP = 0
    indexN = 1
    for i in range(n):
        if arr[i] > 0:
            newarr[indexP] = arr[i]
            indexP += 2
        else:
            newarr[indexN] = arr[i]
            indexN += 2
    print(*newarr)