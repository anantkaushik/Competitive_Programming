"""
Problem Link: https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

Given a linked list of length L. The task is to find the Nth node from the end of the linked list.  
It is needed to complete a method that takes two argument, head of linked list and an integer N. 
There are multiple test cases. For each test case, this method will be called individually.

Input:
First line of input contains number of testcase T. For each testcase, first line of input contains number of nodes 
in the linked list and N. Next line contains nodes of linked list.

Output:
For each testcase, output the data of node which is at Nth distance from end.

User Task:
The task is to complete the function getNthFromLast() which two arguments reference to head and N for which Nth 
from end is to be returned.

Constraints:
1 <= T <= 200
1 <= L <= 103
1 <= N <= 103

Example:
Input:
2
9 2
1 2 3 4 5 6 7 8 9
4 5
10 5 100 5 1

Output:
8
-1

Explanation:
Testcase 1: In the first example, there are 9 nodes in linked list and we need to find 2nd node from end. 
2nd node from end os 8.  
Testcase 2: In the second example, there are 4 nodes in linked list and we need to find 5th from end.  
Since 'n' is more than number of nodes in linked list, output is -1.
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
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(getNthFromLast(head, k))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return index to the any valid peak element
def getNthFromLast(head, n):
    # Code here
    fast = head
    while n and fast:
        fast = fast.next
        n -= 1
    if not fast and not n:
        return head.data
    if not fast:
        return -1
    node = head
    while fast:
        fast = fast.next
        node = node.next
    return node.data
