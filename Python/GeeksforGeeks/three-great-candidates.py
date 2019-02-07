"""
Problem Link: https://practice.geeksforgeeks.org/problems/three-great-candidates/0

The hiring team of Google aims to find 3 candidates who are great collectively. Each candidate has his or her 
ability expressed as an integer. 3 candidates are great collectively if product of their abilities is maximum. 
Given abilities of N candidates, find the maximum collective ability from the given pool of candidates.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follows. 
First line of each test case conatins an interger N  denoting the number of candidates.
The second line of each test case contains N space separated elements denoting the ablities of candidates.

Output:
Corresponding to each test case, print the desired output(maximum collective ability of three candidates) in a newline.

Constraints:
1 ≤ T ≤ 100
3 ≤ N ≤ 107
-105 ≤ ability ≤ 105

Example:
Input
1
6
0 -1 3 100 70 50

Output:
350000
Explanation:
Testcase 1: 70*50*100 = 350000 which is the maximum possible.
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    for i in range(n):
        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max3 = max2
            max2 = arr[i]
        elif arr[i] > max3:
            max3 = arr[i]
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]
    print(max1*max2*max3 if max1*max2*max3 > min1*min2*max1 else min1*min2*max1)