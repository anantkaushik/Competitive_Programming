"""
Problem Link: https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1

You are given an array A of size N. You need to print elements of A in alternate order.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. 
Each test case contains two lines of input. The first line contains N and the second line contains 
the elements of the array.

Output Format:
For each testcase, print the alternate elements of the array(starting from index 0).

Your Task:
Since this is a function problem, you just need to complete the provided function void print(int ar[],int n)

Constraints:
1 <= T <= 200
1 <= N <= 105
1 <= Ai <= 105

Example:
Input:
2
4
1 2 3 4
5
1 2 3 4 5
Output:
1 3
1 3 5

Explanation:
Testcase1: print 1, then 3.
Testcase2: print 1, then 3, then 5.
"""
#Initial Template for Python 3
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    # your code here
    for i in range(0,n,2):
        print(arr[i],end=' ')