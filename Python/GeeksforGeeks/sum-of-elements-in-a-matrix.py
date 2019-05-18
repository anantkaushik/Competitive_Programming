"""
Problem Link:https://practice.geeksforgeeks.org/problems/sum-of-elements-in-a-matrix/0

Given a non null integer matrix,calculate the sum of its elements.

Input: First line contains T , the number of test cases.First line of each test contains 2 integers N,M and N lines follow which 
contain M spaced integers.

Output:Single line for each test case containing the sum

Constraints: 1<= N,M<=10,  -1000<=elements of matrix<=1000

Example:
Input:
1
2 3 
1 0 0
8 -9 -1

Output 
-1
"""
for _ in range(int(input())):
    r,c = map(int,input().split())
    matrix = list(map(int,input().split()))
    summ = 0
    for i in matrix:
        summ += i
    print(summ)