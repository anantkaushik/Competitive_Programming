"""
Problem Link: https://practice.geeksforgeeks.org/problems/sort-a-stack/1

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Input:
The first line of input will contains an integer T denoting the no of test cases . Then T test cases follow. 
Each test case contains an integer N denoting the size of the stack. Then in the next line are N space separated 
values which are pushed to the the stack. 

Output:
For each test case output will be the popped elements from the sorted stack.

Constraints:
1<=T<=100
1<=N<=100

Example(To be used only for expected output):
Input:
2
3
3 2 1
5
11 2 32 3 41

Output:
3 2 1
41 32 11 3 2

Explanation:
For first test case stack will be
1
2
3
After sorting 
3
2 
1

When elements  popped : 3 2 1
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(0), end=" ")
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function sort the stack such that top element is max
# funciton should return nothing
# s is a stack
def sorted(s):
    # Code here
    tempStack = []
    while s:
        temp = s.pop()
        while tempStack and tempStack[-1] > temp:
            s.append(tempStack.pop())
        tempStack.append(temp)
    while tempStack:
        s.append(tempStack.pop())