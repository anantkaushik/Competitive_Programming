"""
Problem Link: https://practice.geeksforgeeks.org/problems/xor-of-all-elements/0

Given an array A[] having n positive elements. The task to create another array B[] such as B[i] is XOR of all elements of array A[] 
except A[i].

Examples:
Input : A[] = {2, 1, 5, 9}
Output : B[] = {13, 14, 10, 6}

Input : A[] = {2, 1, 3, 6}
Output : B[] = {4, 7, 5, 0}


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an 
integer N denoting the size of the array. Then in the next line are N space separated values of the array (B[]).

Output:
For each test case in a new line print the space separated values of the new array (B[]). 

Constraints:
1<=T<=100
1<=N<=100
1<=A[]<=100

Example:
Input:
2
4
2 1 5 9
4
2 1 3 6
Output:
13 14 10 6
4 7 5 0
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    xor = 0
    for no in arr:
        xor ^= no
    for no in arr:
        print(xor^no,end=" ")
    print()