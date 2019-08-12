"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

Given a binary tree, count leaves in it. For example, there are two leaves in below tree

        1
     /      \
   10      39
  /
5

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part 
which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return count of leaves

Constraints:
1 <=T<= 30
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
2
3

There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, 
left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.
"""
#Initial Template for Python 3
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
# Driver Program
if __name__=='__main__':
    
    root = None
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n ==0:
            print(0)
            continue
        dictTree = dict()
        
        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(arr[3*j])
                parent = dictTree[arr[3*j]]
                if j is 0:
                    root = parent
                
            else:
                parent = dictTree[arr[3*j]]
                
            child = Node(arr[3*j+1])
            if (arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child
            
        print(countLeaves(root))
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    # Code here
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)
