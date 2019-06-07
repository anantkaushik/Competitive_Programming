"""
Problem Link: https://practice.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array/0

A sorted array A[ ] with distinct elements is rotated at some unknown point, the task is to find the minimum element in it.

Expected Time Complexity: O(Log n)

Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, 
where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, in a new line, print the minimum element in the array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:
Input
1
5
4 5 1 2 3
Output
1
"""
def minElement(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] < arr[-1]:
        return arr[0]
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < arr[mid-1]:
            return arr[mid]
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        elif arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = end - 1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(minElement(arr))