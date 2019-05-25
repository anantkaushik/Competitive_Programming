"""
Problem Link: https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1

Given a BST,  and a reference to a Node x the task is to find the Inorder Successor of the node . 

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.  
The second line consist of an integer N. Then in the next line are N space separated values of the BST nodes. 
In the next line is an integer x representing the value of the node in the BST.

Output:
For each test case output will be the Inorder successor of the given node. If no such successor is present output will be -1.

Constraints:
1<=T<=100
1<=N<1100
1<=A[]<=1000

Example:
Input:
2
7
20 8 22 4 12 10 14
8
7
20 8 22 4 12 10 14
10
Output:
10
12
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        k = int(input())
        ptr = inorderSuccessor(root, Node(k))
        if ptr is None:
            print(-1)
        else:
            print(ptr.data)


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# your task is to complete this function
# function should return kth smallest element from the BST
def inorderSuccessor(root, n): 
    succ = None
    while root:
        if root.data > n.data:
            succ = root
            root = root.left
        elif root.data < n.data:
            root = root.right
        elif root.data == n.data and root.right:
            return leftMostChild(root.right)
        else:
            break
    return succ
  
def leftMostChild(node): 
    if not node:
        return None
        
    while node.left:
        node = node.left 
    return node