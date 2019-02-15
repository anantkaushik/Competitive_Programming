"""
Problem Link: https://practice.geeksforgeeks.org/problems/find-transition-point/1

You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. 
Transition point is a point where "0" ends and "1" begins.

Input:
You have to complete the method which takes 2 argument: the array arr[] and size of array N. 
You should not read any input from stdin/console. There are multiple test cases. 
For each test cases, this method will be called individually.

Output:
Your function should return transition point.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 500000
0 ≤ C[i] ≤ 1

Example:
Input
1
5
0 0 0 1 1

Output
3
"""
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# finvtion should return an integer
def transitionPoint(arr, n):
    #Code here
    start, end = 0, n-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] == 0:
            start = mid + 1
        else:
            end = mid
    return start