"""
Problem Link: https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. 
The sum list which is a linked list representation of addition of two input numbers.

Input:
First line of input contains number of testcases T. For each testcase, first line of input 
contains length of first linked list and next line contains N elements of the linked list. 
Again, next line contains M, and following line contains M elements of the linked list.

Output:
Output the resultant linked list.

User Task:
The task is to complete the function addTwoLists() which has node reference of both the 
linked lists and returns the head of new list.

Constraints:
1 <= T <= 100
1 <= N, M <= 100

Example:
Input:
2
2
4 5
3
3 4 5
2
6 3
1
7

Output:
0 9 3 
0 7

Explaination:
5->4 // linked list repsentation of 45.
5->4->3 // linked list representation of 345.
0->9 ->3 // linked list representation of 390 resultant linked list.
"""
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
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n_a = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1] # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b =int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list
        result_head = addBoth(a.head,b.head)
        printList(result_head)
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def addBoth(head_a,head_b):
    #code here
    res = Node(0)
    cur = res
    carry = 0
    while head_a or head_b:
        x = head_a.data if head_a else 0
        y = head_b.data if head_b else 0
        summ = carry + x + y
        carry = summ // 10
        cur.next = Node(summ%10)
        cur = cur.next
        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next
    if carry > 0:
        cur.next = Node(carry)
    return res.next