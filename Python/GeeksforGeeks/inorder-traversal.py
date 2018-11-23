"""
Problem Link: https://practice.geeksforgeeks.org/problems/inorder-traversal/1

Given a binary tree, print inorder traversal of it. For example, inorder traversal of below tree is "5 10 1 39"

        1
     /     \
   10       39
  /
5

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part 
which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print inorder traversal.

Constraints:
1 <=T<= 70
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
3 1 2
40 20 60 10 30

There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 
is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right
    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n ==0:
            print()
            continue
        tree = Tree()
        lis=[]
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        inorderTraversal(root)
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the print the nodes which dont have a sibling node
# Note: You aren't required to print a new line after every test case
def inorderTraversal(root):
    # Code here
    if root:
        inorderTraversal(root.left)
        print(root.data,end=" ")
        inorderTraversal(root.right)