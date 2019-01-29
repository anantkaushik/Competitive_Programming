"""
Problem Link: https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1

You are given a pointer/reference to a node to be deleted in a linked list of size N. The task is to delete the node.  
Pointer/reference to head node is not given. 
You may assume that the node to be deleted is not the last node.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains length of 
linked list and next line contains the data of the linked list. The last line contains the node to be deleted.

Output:
For each testcase, print the linked list after deleting the given node.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
2
1 2
1
4
10 20 4 30
20

Output:
2
10 4 30

Explanation:
Testcase 1: After deleting 20 from the linked list, we have remaining nodes as 10, 4 and 30.
"""
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next