"""
Problem Link: https://practice.geeksforgeeks.org/problems/special-stack/1

Design a data-structure SpecialStack (using the STL of stack) that supports all the stack operations like push(), pop(), 
isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. 
Your task is to complete all the functions, using stack data-Structure.

Input Format:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test 
case contains two lines. The first line of input contains an integer n denoting the number of integers in a sequence. 
In the second line are n space separated integers of the stack.

Output Format:
For each testcase, in a new line, print the minimum integer from the stack. 

Your Task:
Since this is a function problem, you don't need to take inputs. Just complete the provided functions.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
1
5
18 19 29 15 16
Output:
15
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''
minStack = []
# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)
    if not minStack or minStack[-1] >= ele:
        minStack.append(ele)
# Function should pop an element from stack
def pop(arr):
    # Code here
    popData = arr.pop()
    if not minStack and minStack[-1] == popData:
        minStack.pop()
    return popData
# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return True if len(arr) == n else False
# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return True if not arr else False
# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    global minStack
    x = minStack[-1]
    minStack = []
    return x