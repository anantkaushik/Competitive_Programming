"""
Problem Link: https://practice.geeksforgeeks.org/problems/smallest-number-subset/0

Given an array A[ ] of N sorted positive integers, find the smallest positive integer S such that S cannot be represented as sum of 
elements of any subset of the given array set.

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases
follow. 
The first line of each test case contains a positive integer N, denoting the length of the array A[ ].
The second line of each test case contains a N space separated positive integers, denoting the
elements of the array A[ ].
Note: The elements of the array should be sorted in ascending order.

Output
Print out the the smallest number S that is not equal to sum of elements of any subset.

Constraints
1 <= T <= 100
0 <   N <= 106
0 <= A[ ] <= 1015
 
Examples 

Input
4
3
1 2 3
4
1 10 12 20
6
3 6 9 10 20 28
5
1 1 1 2 3

Output
7
2
1
9

Explanation:
Testcase 1: 7 is the smallest positive number for which any subset is not present with sum 7.
"""
def getSmallest(arr):
    res = 1
    for no in arr:
        if res >= no:
            res += no
        else:
            return res
    return res
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(getSmallest(arr))