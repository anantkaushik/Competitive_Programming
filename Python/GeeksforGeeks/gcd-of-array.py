"""
Problem Link: https://practice.geeksforgeeks.org/problems/gcd-of-array/0

Given an array of N positive integers. Your task is to find the GCD of all numbers of the array.

Input:
First line of input contains number of test cases T. First line of test case contains a positive integer N, 
size of the array. Next line contains the array elements.

Output:
For each testcase, print the GCD of array elements.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Arr[i] <= 106

Example:
Input:
1
2
5 10

Output:
5

Explanation:
Testcase 1: For array elements 5,10 GCD will be 5.
"""
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(arr[0])
    else:    
        gcdd = gcd(arr[0],arr[1])
        for i in range(2,n):
            gcdd = gcd(gcdd,arr[i])
        print(gcdd)