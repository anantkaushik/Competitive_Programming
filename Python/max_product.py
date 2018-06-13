"""
Given an array with all elements greater than or equal to zero.Return the maximum product of two numbers possible.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, N is size of array.
The second line of each test case contains N input A[i].

Output:
Print the maximum product of two numbers possible.

Example:
Input
1
5
1 100 42 4 23

Output
4200
"""
import heapq
t = int(input())
while t > 0:
    n = input()
    arr = list(map(int,input().split()))
    p = heapq.nlargest(2, arr)
    print(p[0]*p[1])
    t -= 1