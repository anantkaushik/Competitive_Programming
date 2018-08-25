"""
Given an array, swap kth element from beginning with kth element from end.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and k,N is the size of array and kth number.
The second line of each test case contains N input C[i].

Output:
Print the modified array.

Example:
Input
1
8 3
1 2 3 4 5 6 7 8

Output
1 2 6 4 5 3 7 8
"""
t = int(input())
while t > 0:
    l,n = map(int,input().split())
    arr = list(map(int,input().split()))
    arr[n-1],arr[-n] = arr[-n],arr[n-1]
    print(*arr)
    t -= 1