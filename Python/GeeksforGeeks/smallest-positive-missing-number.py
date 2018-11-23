"""
Problem Link: https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0

You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in 
O(n) time using constant extra space.

Input:
First line consists of T test cases. First line of every test case consists of N, denoting the number of elements in array. Second line of every 
test case consists of elements in array.

Output:
Single line output, print the smallest positive number missing.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
5
1 2 3 4 5
5
0 -10 1 3 -20
Output:
6
2
"""
def firstMissingPositive(nums):
    n = len(nums)
    t = [1] + [0] * n
    for i in nums:
        if i >= 1 and i <= n:
            t[i] = 1
    j = 1
    while j <= n:
        if t[j] == 0:
            return j
        j +=1
    return n+1
    
for _ in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    print(firstMissingPositive(arr))