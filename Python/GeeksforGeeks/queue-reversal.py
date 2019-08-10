"""
Problem Link: https://practice.geeksforgeeks.org/problems/queue-reversal/1

Given a Queue Q containing N elements. The task is to reverse the Queue. 
Your task is to complete the function rev(), that reverses the N elements of the queue.

Input Format: 
The first line of input contains an integer T denoting the Test cases. Then T test cases follow. 
The first line contains N which is the number of elements which will be reversed. 
Second line contains N space seperated elements.

Output Format:
For each testcase, in a new line, print the reversed queue.

Your Task:
This is a function problem. You only need to complete the function rev that takes a queue as 
parameter and returns the reversed queue. The printing is done automatically by the driver code.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ elements of Queue ≤ 105

Example:
Input : 
2
6
4 3 1 10 2 6
4
4 3 2 1 

Output : 
6 2 10 1 3 4
1 2 3 4
"""
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        q=list(map(int,input().split()))
        reverseQueue(q)

''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def reverseQueue(q):
    #add code here
    stack = []
    while q:
        stack.append(q.pop(0))
    while stack:
        q.append(stack.pop())
    print(*q)