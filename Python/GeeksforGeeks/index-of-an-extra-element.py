"""
Problem Link: https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1

Given two sorted arrays. There is only 1 difference between the arrays. First array has one element extra added in between. Find the index of the extra element.

Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. 
The first line of each test case contains an integer N, denoting the number of elements in array. 
The second line of each test case contains N space separated values of the array A[]. 
The Third line of each test case contains N-1 space separated values of the array B[].

Output:
Return the index of the corresponding extra element in array A[].(starting index 0).

Constraints:
1<=T<=100
1<=N<=100
1<=Ai<=1000

Example:
Input:
2
7
2 4 6 8 9 10 12
2 4 6 8 10 12
6
3 5 7 9 11 13
3 5 7 11 13
Output:
4
3
"""
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(findExtra(a,b,n))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


def findExtra(a,b,n):
    #add code here
    start = 0
    end = n - 2
    index = n -1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == b[mid]:
            start = mid + 1
        else:
            end = mid - 1
            index = mid
    return index