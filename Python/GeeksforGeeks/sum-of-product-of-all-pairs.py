"""
Problem Link: https://practice.geeksforgeeks.org/problems/sum-of-product-of-all-pairs/0

Given an array A[] of integers find sum of product of all pairs of array elements.

Input:
First line consists of T test cases. First line of every test case consists of N, denoting number of elements of array. 
Second line consists of elements of array.

Output:
Single line output, print the sum of products.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
1
3
1 3 4
Output:
19
"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    summ = 0
    individual_square_sum = 0
    for i in arr:
        summ += i
        individual_square_sum += (i*i)
    array_square = summ * summ
    print((array_square-individual_square_sum)//2)