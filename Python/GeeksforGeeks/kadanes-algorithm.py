"""
Problem Link: https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. 
The first line of each test case contains a single integer N denoting the size of array. 
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 6 of elements (1, 2, 3) which is a contiguous subarray.
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    maxsum = temp = arr[0]
    for i in range(1,len(arr)):
        temp = arr[i] + temp if (arr[i] + temp) > arr[i] else arr[i]
        maxsum = temp if temp > maxsum else maxsum
    print(maxsum)