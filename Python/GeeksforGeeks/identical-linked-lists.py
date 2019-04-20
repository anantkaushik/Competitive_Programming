"""
Problem Link: https://practice.geeksforgeeks.org/problems/identical-linked-lists/1

Given a Singly Linked List of size N. The task is to complete the function areIdentical(), which checks whether two linked list are identical or not. 
Two Linked Lists are identical when they have same data and arrangement of data is also same.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of linked lists N and M and next 
line contains elements of the linked lists.

Output:
For each test the output will be 'Identical' if two list are identical else 'Not identical'.

User Task:
The task is to complete the function areIdentical() which takes head of both linked lists as arguments and returns True or False.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
6
1 2 3 4 5 6
4
99 59 42 20
5
1 2 3 4 5
5
1 2 3 4 5

Output:
Not identical
Identical

Explanation:
Testcase 1: Each element of first linked list is not equal to each elements of second linked list in the same order.
Testcase 2: Each element of first linked list is equal to each elements of second linked list in the same order.
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
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if(areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
def areIdentical(head1, head2):
    # Code here
    if not head1 and not head2:
        return True
    if head1.data != head2.data:
        return False
    return areIdentical(head1.next,head2.next)