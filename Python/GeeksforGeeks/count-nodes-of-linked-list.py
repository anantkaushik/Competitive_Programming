"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1

Given a singly linked list. The task is to find the length of linked list, where length is defined as number of 
nodes in the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of nodes N, 
to be inserted into the linked list and next line contains data of N nodes.

Output:
There will be a single line of output for each testcase, which contains length of the linked list.

Constraints:
1 <= T <= 30
1 <= N <= 100
1 <= value <= 103

User Task:
Your task is to complete the given function getCount(), which takes head reference as argument and should 
return the length of linked list.

Example:
Input:
2
5
1 2 3 4 5
7
2 4 6 7 5 1 0

Output:
5
7

Explanation:
Testcase 1: Count of nodes in the linked list is 5, which is its length.
"""
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
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
        n = int(input())
        value = list(map(int, input().split()))
        for i in reversed(value):
            llist.push(int(i))
        k = getCount(llist.head)
        print(k)
        T -= 1

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

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
# head is reference to head of linked list
def getCount(head):
    # Code here
    # count = 0
    # while head:
    #     count += 1
    #     head = head.next
    # return count
    if not head:
        return 0
    return 1 + getCount(head.next)