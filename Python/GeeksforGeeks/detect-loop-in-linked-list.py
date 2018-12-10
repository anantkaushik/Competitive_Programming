"""
Problem Link: https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

Given a linked list, check if the the linked list has a loop. Linked list can contain self loop.

Input:
In this problem, method takes one argument: the head of the linked list. The function should not read any input from 
stdin/console.The node structure has a data part which stores the data and a next pointer which points to the next 
element of the linked list. There are multiple test cases. For each test case, this method will be called individually.

Output:
Return 1 if linked list has a loop else 0.

Constraints:
1<=T<=50
1<=N<=300

Example:
Input:
2
3
1 3 4
2
4
1 8 3 4
0
Output:
True
False

Explaination:
In above test case N = 3
The linked list with nodes N = 3 is given. Then value of x=2 is given which means last node is connected with 
xth node of linked list. Therefore, there exists a loop. 
For N = 4
x = 0 means then lastNode->next = NULL, then the Linked list does not contains any loop.
"""
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
        if detectLoop(lst.getHead()):
            print(True)
        else:
            print(False)

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Functioon should return 1/0 or True/False
def detectLoop(head):
    # code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False