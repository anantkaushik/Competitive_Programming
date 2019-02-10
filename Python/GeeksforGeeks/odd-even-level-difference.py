"""
Problem Link: https://practice.geeksforgeeks.org/problems/odd-even-level-difference/1

Given a a Binary Tree, your task is to complete the function getLevelDiff which returns the difference between the sum of nodes at odd level and 
the sum of nodes at even level . The function getLevelDiff  takes only one argument  ie the root of the binary tree . 
       2
     /   \
    3     5
For the above tree the odd level sum is 2 and even level sum is 8 thus the difference is 2-8=-6

Input:
The task is to complete the method which takes one argument, root of Binary Tree. There are multiple test cases. 
For each test case, this method will be called individually.

Output:
The function should return an integer denoting the difference between the sum of nodes at odd level and the sum of nodes at even level

Constraints:
1 <=T<= 30
1 <= Number of nodes<= 20

Example:
Input
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output
-4
60

There are two test cases. First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.
Second test case represents a tree with 4 edges and 5 nodes.
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
class Tree:  # Binary tree Class
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
    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data, end=" ")
            self.traverseInorder(root.right)
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
            k+=3
        # tree.traverseInorder(root)
        # print ''
        print(getLevelDiff(root))

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should return an integer
def getLevelDiff(root):
    # Code here
    if not root:
        return 0
    return (root.data - getLevelDiff(root.left) - getLevelDiff(root.right))