"""
Problem Link: https://practice.geeksforgeeks.org/problems/occurence-of-an-integer-in-a-linked-list/1

Given a singly linked list and a key, count number of occurrences of given key in linked list. 
For example, if given linked list is 1->2->1->2->1->3->1 and given key is 1, then output should be 4.

Input:
You have to complete the method which takes two argument: the head of the linked list and int k. 
You should not read any input from stdin/console.
The struct Node has a data part which stores the data and a next pointer which points to the 
next element of the linked list. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
You have to count a number of occurrences of given key in linked list and return the count value.

Note: If you use "Test" or "Expected Output Button" use below example format

Example:
Input:
1
8
1 2 2 4 5 6 7 8
2

Output:
2
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        m = int(input())
        k = count(llist.head, m)
        print(k)
        t -= 1

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""  Return the no. of times search_for value is there in a linked list.
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def count(head, search_for):
    # Code here
    count = 0
    while head:
        if head.data == search_for:
            count += 1
        head = head.next
    return count