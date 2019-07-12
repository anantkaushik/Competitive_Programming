"""
Problem Link: https://practice.geeksforgeeks.org/problems/node-at-a-given-index-in-linked-list/1

Given a singly linked list with N nodes and a number X. The task is to find the node at the given index (X)(1 based index) of linked list. 

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains space seperated two integers, 
length of linked list and X.

Output:
For each testcase, there will be single line of output containing data at Xth node.

User Task:
The task is to complete the function GetNth() which takes head reference and index as arguments and should return the data at Xth 
position in the linked list.

Constraints:
1 <= T <= 30
1 <= N <= 100
K <= N
1 <= value <= 103

Example:
Input:
2
6 5
1 2 3 4 657 76
10 2
8 7 10 8 6 1 20 91 21 2

Output:
657
7

Explanation:
Testcase 1: Element at 5th index in the linked list is 657 (1-based indexing).
"""
{
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
if __name__ == '__main__':
    llist = LinkedList()
    T = int(input())
    while (T > 0):
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        value = list(map(int, input().split()))
        for i in reversed(value):
            llist.push(int(i))
        m = getNth(llist.head, k)
        print(m)
        T -= 1
        

}
''' This is a function problem.You only need to complete the function given below '''
"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
def getNth(head, k):
    # Code here
    k -= 1
    while head and k:
        head = head.next
        k -= 1
    return head.data