"""
Problem Link: https://practice.geeksforgeeks.org/problems/product-array-puzzle

Given an array A of size N, construct a Product Array P (of same size) such that P is equal to the product of 
all the elements of A except A[i].

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. 
Each testcase contains two lines of input. The first line is N. The second line contains N elements 
separated by spaces.

Output:
For each testcase, print the Product array P.

Constraints:
1 <= T <= 10
1 <= N <= 1000
1 <= Ai <= 20

Example:
Input
2
5
10 3 5 6 2
2
12 20
Output
180 600 360 300 900
20 12

Explanation:
Testcase1: For the product array P, at i=0 we have 3*5*6*2. At i=1 10*5*6*2. At i=2 we have 10*3*6*2. 
At i=3 we have 10*3*5*2. At i=4 we have 10*3*5*6 So P is 180 600 360 300 900
"""
def productExceptSelf(arr):
    p = 1
    res = []
    for i in range(len(arr)):
        res.append(p)
        p *= arr[i]
    p = 1
    for i in range(len(arr)-1,-1,-1):
        res[i] *= p
        p *= arr[i]
    return res
    
for _ in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    print(*productExceptSelf(arr))