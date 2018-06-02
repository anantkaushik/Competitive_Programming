"""
Given an array A[N], you are required to sort the array in given index range [a, b], i.e., 
you need to sort subarray A[a..b]
Input : 
The first line of input contains an integer T denoting the Test cases. Then T test cases follow. 
The first line contains an integer N i.e number of array elements.
The second line contains array elements A[i]
The third line contains a and b

Output : 
For each test case, the output is the sorted array as per the given range [a, b] 

Input : 
1
5
7 8 4 5 2
1 4

Output : 
7 2 4 5 8
"""
t = int(input())
while t > 0:
    n = input()
    arr = list(map(int,input().split()))
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    x = arr[a:b+1]
    x.sort()
    arr[a:b+1] = x
    print(*arr)
    t -= 1