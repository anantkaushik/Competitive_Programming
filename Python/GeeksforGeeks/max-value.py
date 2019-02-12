"""
Problem Link: https://practice.geeksforgeeks.org/problems/max-value/0

  
In a given array A[] find the maximum value of (A[i] – i) - (A[j] – j) where i is not equal to j. 
i and j vary from 0 to n-1 and N is size of input array A[].  Value of N is always greater than 1.

Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consist of two lines. 
The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.

Output:
Corresponding to each test case, in a new line, print the maximum value.

Constraints:
1 ≤ T ≤ 100
2 ≤ N ≤ 200
1 ≤ A[i] ≤ 1000

Example:
Input
1
5
9 15 4 12 13

Output
12     

Explanation
(a[1]-1) - (a[2]-2) = (15-1)-(4-2) = 12
"""
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    minn,maxx = 10001, -1
    for i in range(n):
        if a[i] - (i + 1) > maxx:
            maxx = a[i] - (i + 1)
        if a[i] - (i + 1) < minn:
            minn = a[i] - (i + 1)
    print(maxx - minn)