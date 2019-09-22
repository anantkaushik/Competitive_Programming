"""
Problem Link: https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/

There are two singly linked lists of size N and M in a system. But, due to some programming 
error the end node of one of the linked list got linked into one of the node of second list, 
forming a inverted Y shaped list. Write a program to get the point where two linked lists 
intersect each other.

Input:
First line of input is the number of test cases T. Every test case has four lines. 
First line of every test case contains three numbers, x (number of nodes before 
merge point in 1st list), y (number of nodes before merge point in 11nd list) 
and z (number of nodes after merge point). Next three lines contain x, y and z values.

Output:
Print the data of the node in the linked list where two linked lists intersects.

Your Task:
The task is to complete the function intersetPoint() which finds the point of intersection 
of two linked list. The function should return data value of a node where two linked lists merge. 
If linked list do not merge at any point, then it shoudl return -1.

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= value <= 1000

Example:
Input:
2
2 3 2
10 20
30 40 50
5 10
2 3 2
10 20
30 40 50
10 20

Output:
5
10

Explanation:
Testcase 1: The point of intersection of two linked list is 5, means both of them get 
linked (intersects) with each other at node whose value is 5.
"""
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
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
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))
        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list
        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list
        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        if intersetPoint(a.head,b.head) == -1:
            print(-1)
        else:
            print(intersetPoint(a.head,b.head).data) #print data present at the node.
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
	Your task is to return the point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: NODE present at the point of intersection, or -1 if no common point.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def intersetPoint(head_a,head_b):
    #code here
    APointer = head_a
    BPointer = head_b
    while APointer != BPointer:
        APointer = APointer.next if APointer.next else head_b
        BPointer = BPointer.next if BPointer.next else head_a
    return APointer