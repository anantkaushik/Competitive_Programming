"""
Given an array, find the largest element in it.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n , the no of elements in the array. Then next line contains n integers of the array.

Output:
Print the maximum element in the array.

Example:
Input:
2
5
10 324 45 90 9808
7
1 2 0 3 2 4 5

Output :
9808
5
"""
t = int(input())
while t > 0:
    n = input()
    arr = list(map(int,input().split()))
    print(max(arr))
    t -= 1