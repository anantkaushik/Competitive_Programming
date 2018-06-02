"""
GIven two different arrays A and B your task is to merge the two arrays which are unsorted into 
another array which is sorted.

Input:

The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. The first line of each test case contains the integers N and M 
denoting the size of arrays A and B respectively.
The second line of each test case contains N space separated integers denoting elements of the array A[ ].
The third line of each test case contains M space separated integers denoting elements of the array B[ ].

Output:
Print the merged and sorted array with space between each element. 
Print the answer for each test case in a new line.

Example:
Input:
1
3 3
10 5 15
20 3 2
Output:
2 3 5 10 15 20
"""
t = int(input())
while t > 0:
    a = input()
    x = list(map(int,input().split()))
    x += list(map(int,input().split()))
    x.sort()
    print(*x)
    t -= 1