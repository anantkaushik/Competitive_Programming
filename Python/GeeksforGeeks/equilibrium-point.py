"""
Problem Link: https://practice.geeksforgeeks.org/problems/equilibrium-point/0/

Given an array A of N positive numbers. The task is to find the position where equilibrium 
first occurs in the array. Equilibrium position in an array is a position such that the 
sum of elements before it is equal to the sum of elements after it.

Input:
The first line of input contains an integer T, denoting the number of test cases. 
Then T test cases follow. First line of each test case contains an integer N denoting 
the size of the array. Then in the next line are N space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium 
if no equilibrium point exists print -1.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 108

Example:
Input:
2
1
1
5
1 3 5 2 2

Output:
1
3

Explanation:
Testcase 1: Since its the only element hence its the only equilibrium point.
Testcase 2: For second test case equilibrium point is at position 3 as elements 
below it (1+3) = elements after it (2+2).
"""
def findEquilibrium(arr):
    right_sum = sum(arr)
    index = 0
    left_sum = 0
    for i in range(len(arr)):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return i+1
        left_sum += arr[i]
    return -1
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(findEquilibrium(arr))