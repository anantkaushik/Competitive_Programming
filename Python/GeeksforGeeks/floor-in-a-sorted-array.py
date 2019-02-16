"""
Problem Link: https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array/0

Given a sorted array arr[] without duplicates, and a value x. Find the floor of x in given array.
Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains 
number of elements in the array and element whose floor is to be searched. Last line of input contains array elements.

Output:
Output the index of floor of x if exists, else print -1.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]

Example:
Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
-1
1
3

Explanation:
Testcase 1: No element less than 0 is found. So output is "-1".
Testcase 2: Number less than 5 is 2, whose index is 1(0-based indexing).
"""
for _ in range(int(input())):
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    start,end = 0, n-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    print(end)