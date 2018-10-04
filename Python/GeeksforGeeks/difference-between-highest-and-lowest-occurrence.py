"""
Given an array, the task is to find the difference between highest occurrence and 
lowest occurrence of any number in an array.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of two lines. First line of each 
test case contains a integer N and the second line contains N space separated array elements.

Output:
For each test case, print the difference in new line.

Example:
Input:
2
3
1 2 2
6
1 2 2 3 3 3

Output:
1
2
"""
import collections
t = int(input())
while t > 0:
    input()
    arr = list(map(int,input().split()))
    d = collections.Counter(arr)
    l = list(d.values())
    print(max(l)-min(l))
    t -= 1