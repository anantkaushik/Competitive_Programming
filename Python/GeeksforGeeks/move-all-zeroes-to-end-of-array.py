"""
Problem Link: https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array/0

Given an array A of positive integers. Push all the zero’s of a given array to the end of the array.

Input:
The first line contains an integer T denoting the total number of test cases. 
In each test cases, first line is number of elements in array N and next line contains array elements.

Output:
Print the array after shifting all 0's at the end.â€‹

Constraints:
1 <= T <= 100
1 <= N <= 103
0 <= Ai <=103

Example:
Input:
1
5
3 5 0 0 4

Output:
3 5 4 0 0

Explanation:
Testcase 1: All the zeros are moved to last and then array is as shown in the output.
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    index = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[index] = arr[index],arr[i]
            index += 1
    print(*arr)