"""
Problem Link: https://practice.geeksforgeeks.org/problems/size-of-binary-tree/1

Given a binary tree, count number of nodes in it. For example, count of nodes in below tree is 4.

        1
     /      \
   10      39
  /
5
Your task is to complete the function getSize() which accepts root node of the tree, and returns the size.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. 
The first line contains E, number of edges. The second line contains E+1 nodes of the binary tree separated by space. 
The left and right nodes of tree are referred as such 1 2 L 1 3 R i.e 2 is left of 1 and 3 is right of 1.

Output:
For each testcase in new line, print the number of nodes.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function getSize().

Constraints:
1 <= T <= 30
1 <= E <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
2
1 2 L 1 3 R
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
3
5

Explanation:
Testcase 1: First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 2 and right child of 1 is 3
"""
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
class Tree:
    def createNode(self, data):
        return (Node(data))
    
    def insert(self, node, data, ch):
        if (node is None):
            return (self.createNode(data))
        if(ch=='L'):
            node.left = self.insert(node.left, data, ch)
            return (node.left)
        else:
            node.right = self.insert(node.right, data, ch)
            return (node.right)
    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if (i.data == data):
                return (i)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
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
            # print (arr[k], arr[k+1], ptr)
            k+=3
        print (size(root))

''' This is a function problem.You only need to complete the function given below '''
# Your task to complete this function
# function should return size of the binary tree as integer
def size(node):
    # code here
    if not node:
        return 0
    return (1 + size(node.left) + size(node.right))