"""
Problem Link: https://practice.geeksforgeeks.org/problems/bubble-sort/1

The task is to complete bubble function which is used to implement Bubble Sort!

Input Format:
First line of the input denotes the number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.

Output Format:
For each testcase, in a new line, print the sorted array.

Your Task:
This is a function problem. You only need to complete the function bubble that sorts the array. Printing is done automatically by the driver code.

Constraints:
1 <=T<= 100
1 <=N<= 103
1 <=arr[i]<= 103

Example:
Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1
Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10
"""
{
#Initial Template for Python 3
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def bubbleSort(arr, n):
    # code here
    for i in range(n-1):
        arr = bubble(arr, i, n)
    return arr
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr = bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print ('')

}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
'''Your task is to complete the bubble function
   which is used in bubbleSort() Function'''
'''def bubbleSort(arr, n):
    for i in range(n-1):
        arr = bubble(arr, i, n)
    return arr'''
# Function should return the array
def bubble(arr, i, n):
    # code here
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
    return arr