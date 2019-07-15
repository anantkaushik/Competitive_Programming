"""
Problem Link: https://practice.geeksforgeeks.org/problems/insert-in-middle-of-linked-list/1

Given a linked list of size N and a key. The task is to insert the key in the middle of the linked list.

Input Format:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list N and next line contains N elements to be 
inserted into the linked list and the last line contains the element to be inserted to the middle.

Output Format:
For each testcase, there will be a single line of output containing the element of modified linked list.

User Task:
The task is to complete the function insertInMiddle() which takes head reference and element to be inserted as the arguments. The printing is done 
automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
3
1 2 4
3
4
10 20 40 50
30

Output:
1 2 3 4
10 20 30 40 50

Explanation:
Testcase 1: The new element is inserted after the current middle element in the linked list.
"""
{
#Initial Template for Python 3
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
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        mid_elem = int(input())
        insertInMid(a.head, Node(mid_elem) )
        a.printList()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node (node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
def insertInMid(head,node):
    #code here
    fast = head.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    node.next = slow.next
    slow.next = node
    return head