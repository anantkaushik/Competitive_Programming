"""
Problem Link: https://practice.geeksforgeeks.org/problems/mirror-tree/1

Input:
The task is to complete the method that takes one argument, root of Binary Tree and modifies the tree.

Output:
The function should conert the tree to its mirror

Constraints:
1 <=T<= 75
1 <= Number of nodes<= 100
1 <= Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
2 1 3
30 10 60 20 40
There are two test casess.  First case represents a tree with 3 nodes, 2 edges. Here root is 1, left child of 1 is 3 and right child of 1 is 2.
Second test case represents a tree with 4 edges and 5 nodes.
"""
#Initial Template for Python 3
class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None
def inorderTraversalUtil(root):
    # Code here
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)
def inorderTraversal(root):
    # Code here
    inorderTraversalUtil(root)
    print()
if __name__ == '__main__':
    t = int(input())
    
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        
        root = None
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]
                
                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]
            
            child = Node(int(arr[3*j+1]))
                
            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
                
        mirror(root)
        
        inorderTraversal(root)

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
def mirror(root):
    if not root:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    mirror(root.left)
    mirror(root.right)