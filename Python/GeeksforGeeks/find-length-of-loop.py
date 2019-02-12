"""
Problem Link: https://practice.geeksforgeeks.org/problems/find-length-of-loop/1

Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given 
Linked List contains loop or not and if loop is present then return the count of nodes in loop or else return 0.

Input(to be used for Expected Output Only):
First line of input contains number of testcases T. For each testcase, first line of input contains length of 
linked list and next line contains data of the linked list.

Output:
For each testcase, there will be a single line of output containing the length of loop in linked list, else print 0, 
if loop is not present in the linked list.

User Task:
The task is to complete the function countNodesinLoop() which contains the only argument as reference to head of 
linked list.

Constraints:
1 <= T <= 100
1 <= N <= 500

Example:
Input:
2
10
25 14 19 33 10 21 39 90 58 45
4
2
1 0
1
Output:
6
1

Explanation:
Testcase 1: There is a loop of length 6 in the given linked list.
"""
#Initial Template for Python 3
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # Utility function to prit the linked LinkedList
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
    def getHead(self):
        return self.head
    def createLoop(self, n):
        if n == 0:
            return None
        temp = self.head
        ptr = self.head
        cnt = 1
        while (cnt != n):
            ptr = ptr.next
            cnt += 1
        # print ptr.data
        while (temp.next):
            temp = temp.next
        temp.next = ptr
# Driver program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lst = LinkedList()
        for i in arr:
            lst.push(i)
        ele = int(input())
        lst.createLoop(ele)
        print(countNodesinLoop(lst.getHead()))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
##Complete this function
def countNodesinLoop(head):
    # code here
    if not head:
        return 0
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not fast:
        return 0
    if not fast.next:
        return 0
    count = 0
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next
    return count