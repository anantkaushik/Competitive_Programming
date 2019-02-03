"""
Problem Link: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. 
Each testcases contains two lines of input. The first line denotes the size of the array N. 
The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints: 
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    left, right = 0, n-1
    index = 0
    while left <= right:
        while arr[right] == 2 and left <= right:
            right -= 1
        if arr[left] == 2 and left <= right:
            arr[right], arr[left] = arr[left], arr[right]
            right -= 1
        if arr[left] == 0 and left <= right:
            arr[index], arr[left] = arr[left], arr[index]
            index += 1
        left += 1
    print(*arr)