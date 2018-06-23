"""
Given an array which contains all elements occurring k times, but one occurs only once. 
Find that unique element.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each 
test case consists of two integers n and k. The next line consists of n spaced integers. 

Output:
Print the required output.

Example:
Input:
2
7 3
6 2 5 2 2 6 6 
5 4
2 2 2 10 2

Output:
5
10
"""
import collections
t = int(input())
while t > 0:
    input()
    arr = list(map(int,input().split()))
    c = collections.Counter(arr)
    for key, value in c.items():
        if value == 1:
            print(key)
            break
    t -= 1