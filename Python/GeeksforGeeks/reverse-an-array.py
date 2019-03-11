"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-an-array/0

Given an array A of size N, print the reverse of it.

Input:
First line contains an integer denoting the test cases 'T'. T testcases follow. 
Each testcase contains two lines of input. First line contains N the size of the array A. 
The second line contains the elements of the array.

Output:
For each testcase, in a new line, print the array in reverse order.

Constraints:
1 <= T <= 100
1 <= N <=100
0 <= Ai <= 100

Example:
Input:
1
4
1 2 3 4
Output:
4 3 2 1
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(*arr[::-1])
    start,end = 0, n - 1
    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(*arr)