"""
Problem Link: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

Given a linked list of length N. The task is to reverse the list.

Input:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list 
and next line contains the elements of linked list.

Output:
Reverse the linked list and return head of the modified list.

User Task:
The task is to complete the function reverse() which head reference as the only argument and should return 
new head after reversing the list.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
1
6
1 2 3 4 5 6

Output:
6 5 4 3 2 1

Explanation:
Testcase 1: After reversing the list, elements are as 6->5->4->3->2->1.
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.lastNode = None
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node
    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head
    reverse_List = reverseList
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#function Template for python3
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
# your task is to complete this function
# function shouldn't return anything
# use self.head to access head in the method
def reverseList(self):
    # Code here
    if self.head is None:
        return None
    prev = None
    while self.head:
        temp = self.head.next
        self.head.next = prev
        prev = self.head
        self.head = temp
    self.head = prev