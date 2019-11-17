"""
Problem Link: https://practice.geeksforgeeks.org/problems/maximum-difference/0

You are given an array A (distinct elements) of size N. Find out the maximum difference 
between any two elements such that larger element appears after the smaller number in A.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. 
Each testcase contains two lines of input. The first line of each test case is N,N is the size of array. The second line of each test case contains N elements separated by spaces.

Output:
For each testcase, print the maximum difference between two element. Otherwise print -1

Constraints:
1 <= T <= 100
2 <= N <= 107
0 <= Ai <= 107

Example:
Input:
2
7
2 3 10 6 4 8 1
6
7 9 5 6 3 2

Output:
8
2
Explanation:
Testcase1:  Array is [2, 3, 10, 6, 4, 8, 1] then returned value is 8 (Diff between 10 and 2).
Testcase2: Array is [ 7, 9, 5, 6, 3, 2 ] then returned value is 2 (Diff between 7 and 9).
"""
def maxDifference(arr):
    maxDiff = -1
    curMin = arr[0]
    for i in range(1,len(arr)):
        maxDiff = max(maxDiff,arr[i]-curMin)
        if arr[i] < curMin:
            curMin = arr[i]
    return maxDiff

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(maxDifference(arr))