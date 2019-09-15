"""
Problem Link: https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/

Given an array of 0's and 1's your task is to complete the function maxLen which returns 
size of the largest sub array with equal number of 0's and 1's. The function maxLen 
takes 2 arguments. The first argument is the array A[] and second argument is the 
size 'N' of the array A[].

Input:
The first line of the input is T denoting the number of test cases. Then T test cases follow.
Each test case contains two lines. The first line of each test case is a number N denoting 
the size of the array and in the next line are N space separated values of A [].

Output:
For each test case output in a new line the max length of the subarray.

Constraints:
1 <= T <= 100
1 <= N <= 100
0 <= A[] <= 1

Example:
Input
2
4
0 1 0 1
5
0 0 1 0 0

Output
4
2

Explanation:
Testacase 1: The array from index [0...3] contains equal number of 0's and 1's. 
Thus maximum length of subarray having equal number of 0's and 1's is 4.
"""
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n, arr))
''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
# Function should return an integer
def maxLen(n, lis):
    #code here
    d = {}
    d[0] = -1
    maxLen = count = 0
    for i in range(len(lis)):
        count += 1 if lis[i] == 1 else -1
        if count in d:
            maxLen = max(maxLen, i-d[count])
        else:
            d[count] = i
    return maxLen
    
