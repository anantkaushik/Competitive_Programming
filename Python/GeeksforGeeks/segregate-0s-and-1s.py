""" 
Problem Link: https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s/0

You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].

Output:
Print 0s on left side and 1s on right side.

Sample Input:
2
5
0 0 1 1 
4
1 1 1 1

Sample Output:
0 0 0 1 1
1 1 1 1
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    pos = -1
    for i in range(n):
        if arr[i] == 0:
            pos+=1
            arr[i],arr[pos] = arr[pos],arr[i]
    print(*arr)