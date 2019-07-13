"""
Problem Link: https://practice.geeksforgeeks.org/problems/linked-list-insertion/1

Given a key (or data) to be inserted into the linked list of size N. The task is to insert the element at head or tail of the linked 
list depending on the input just before it p. If p is 0, then insert the element at beginning else insert at end.
Hint : When inserting at the end, make sure that you handle NULL explicitly.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked list N and next 
line contains 2*N integers, each element to be inserted into the list is preceded by a 0 or 1 which decide the place to be inserted.

Output Format:
For each testcase, there will be a single line of output which contains the linked list elements.

Your Task:
This is a function problem. You only need to complete the functions insertAtBeginning and insertAtEnd that returns head after successful 
insertion. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
3
5
9 0 5 1 6 1 2 0 5 0
3
5 1 6 1 9 1
4
15 0 36 0 95 0 14 0

Output:
5 2 9 5 6
5 6 9
14 95 36 15

Explanation:
Testcase 1: After inserting the elements at required position, we have linked list as 5, 2, 9, 5, 6.
"""
{
#Contributed by : Nagendra Jha
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
#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        nodes_info=list(map(int,input().strip().split()))
        for i in range(0,len(nodes_info)-1,2):
            if(nodes_info[i+1]==0):
                insertAtBegining(a,nodes_info[i])
            else:
                insertAtEnd(a,nodes_info[i])
        a.printList()
}
''' This is a function problem.You only need to complete the function given below '''
'''
	Your task is to complete both
	these functions given below.
	Function Arguments: a (linked list) and value (value to be inserted)
	Return Type: None
'''
'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# function should insert new node at the
# beigning of the list
def insertAtBegining(a,value):
    #code here
    node = Node(value)
    node.next = a.head
    a.head = node
    
    
# function should insert new node at the
# end of the list
def insertAtEnd(a,value):
    #code here too :)
    cur = a.head
    if not cur:
        a.head = Node(value)
    else:
        while cur.next:
            cur = cur.next
        cur.next = Node(value)