"""
Problem Link: https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1

Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge 
both of the list (in-place) and return head of the merged list.
Note: It is strongly recommended to do merging in-place using O(1) extra space.

Input:
First line of input contains number of testcases T. For each testcase, first line of 
input contains N and M, and next two line contains N and M sorted elements in two lines for each.

Output:
For each testcase, print the merged list in sorted form.

User Task:
The task is to complete the function sortedMerge() which takes references to the heads of 
two linked lists as the arguments and returns the head of merged linked list.

Constraints:
1 <= T <= 200
1 <= N, M <= 103
1 <= Node's data <= 103

Example:
Input:
2
4 3
5 10 15 40 
2 3 20
2 2
1 1
2 4 

Output:
2 3 5 10 15 20 40
1 1 2 4

Explanation:
Testcase 1: After merging the two linked lists, we have merged list as 2, 3, 5, 10, 15, 20, 40.
"""
#Initial Template for Python 3
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
        n,m = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        for x in nodes_b:
            b.append(x)
        a.head = merge(a.head,b.head)
        a.printList()
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def merge(head_a,head_b):
    #code here
    if not head_a or not head_b:
        return head_a or head_b
    newHead = Node(0)
    prev = newHead
    while head_a and head_b:
        if head_a.data < head_b.data:
            prev.next = head_a
            prev = head_a
            head_a = head_a.next
        else:
            prev.next = head_b
            prev = head_b
            head_b = head_b.next
    prev.next = head_a or head_b
    return newHead.next