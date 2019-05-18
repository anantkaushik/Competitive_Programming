"""
Problem Link: https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not/0

Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal 
if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. 
Each test case contains 3 lines of input. The first line contains an integer N denoting the size of the array. 
The second line contains element of array A[]. The third line contains elements of the array B[].

Output:
For each test case, print 1 if the arrays are equal else print 0.

Constraints:
1<=T<=100
1<=N<=107
1<=A[],B[]<=1018

Example:
Input:
2
5
1 2 5 4 0
2 4 5 0 1
3
1 2 5
2 4 15
Output:
1
0

Explanation:
Testcase1:
Input : A[] = {1, 2, 5, 4, 0}; B[] = {2, 4, 5, 0, 1};
Output : 1
Testcase2:
Input : A[] = {1, 2, 5}; B[] = {2, 4, 15};
Output : 0
"""
def isSame(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    check = 0
    sum1 = 0
    sum2 = 0
    for n in arr1:
        check ^= n
        sum1 += n
    for n in arr2:
        check ^= n
        sum2 += n
    return True if not check and sum1 == sum2 else False 
    
for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print(1 if isSame(arr1,arr2) else 0)