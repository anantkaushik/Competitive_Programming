"""
Problem Link: https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1

Given a singly linked list of size N. The task is to rotate the linked list counter-clockwise by k nodes,
where k is a given positive integer smaller than or equal to length of the linked list.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains length of 
linked list and next line contains linked list elements and last line contains k, by which linked list is to be rotated.

Output Format:
For each testcase, print the rotated linked list.

User Task:
The task is to complete the function rotate() which takes head reference as the first argument and k as the second argument. 
The printing is done automatically by the driver code.

Constratints:
1 <= T <= 100
1 <= N <= 103
1 <= k <= 103

Example:
Input:
3
8
1 2 3 4 5 6 7 8
4
5
2 4 7 8 9
3
2
1 2
4

Output:
5 6 7 8 1 2 3 4
8 9 2 4 7
1 2

Explanation:
Testcase 1: After rotating the linked list by 4 elements (anti-clockwise), we reached to node 5, which is (k+1)th node 
from beginning, now becomes head and tail of the linked list is joined to the previous head.
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
        while(temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")
if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1

''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
# This function should rotate list counter-
# clockwise by k and return new head (if changed) 
def rotateList(head, k):
    # code here
    if not head:
        return None
    l = length(head)
    k = k%l
    if not k:
        return head
    cur = head
    for _ in range(k-1):
        cur = cur.next
    newHead = cur.next
    newCur = cur.next
    cur.next = None
    while newCur.next:
        newCur = newCur.next
    newCur.next = head
    return newHead
    
def length(head):
    l = 0
    while head:
        l += 1
        head = head.next
    return l