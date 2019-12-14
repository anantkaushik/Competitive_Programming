"""
Problem Link: https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1

Given K sorted linked lists of different sizes. The task is to merge them in such a 
way that after merging they will be a single sorted linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line 
of input contains number of linked lists N and next line contains data of nodes of 
all K linked lists, with first element as M, the length of linked list and 
next M elements for the same linked list.

Output:
For each testcase, in a new line, print the merged linked list.

Your Task:
The task is to complete the function mergeKList() which merges the K given lists into a sorted one. 
The printing is done automatically by the driver code.

Constraints
1 <= T <= 50
1 <= N <= 103

Example:
Input:
2
4
3 1 2 3 2 4 5 2 5 6 2 7 8
3
2 1 3 3 4 5 6 1 8

Output:
1 2 3 4 5 5 6 7 8
1 2 3 4 5 6 8

Explanation :
Testcase 1: The test case has 4 sorted linked list of size 3, 2, 2, 2
1st    list     1 -> 2-> 3
2nd   list      4->5
3rd    list      5->6
4th    list      7->8
The merged list will be 1->2->3->4->5->5->6->7->8.
"""
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
        n = int(input())
        a= []
        for i in range(n):
            a.append(LinkedList())
        list_info = list(map(int,input().strip().split()))
        curr_ind = 0
        curr_list_ind = 0
        while curr_ind < len(list_info):
            nodes= list_info[curr_ind]
            curr_ind+=1
            for i in range(nodes):
                a[curr_list_ind].append(list_info[curr_ind])
                curr_ind += 1
            curr_list_ind += 1
        heads = []
        for i in range(n):
            heads.append(a[i].head)
        printList(merge(heads,n))

''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the head of the new formed linked list.
	
	Function Arguments: array "heads" (containing heads of linked lists), n size of array a.
	Return Type: head node.;
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def merge(lists,n):
    if not lists: return None
    length = len(lists)
    interval = 1
    while interval < length:
        for i in range(0, length - interval, interval*2):
            lists[i] = mergeLists(lists[i], lists[i+interval])
        interval *= 2
    return lists[0]
      
def mergeLists(l1, l2):
  if not l1 or not l2:
    return l1 or l2
  head = Node(0)
  cur = head
  while l1 and l2:
    if l1.data < l2.data:
      cur.next = l1
      l1 = l1.next
    else:
      cur.next = l2
      l2 = l2.next
    cur = cur.next
  if l1 or l2:
    cur.next = l1 or l2
  return head.next