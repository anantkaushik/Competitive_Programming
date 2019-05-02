"""
Problem Link: https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1

Given two binary trees, the task is to find if both of them are identical or not. 

Input:
The task is to complete the method isIdentical(), which takes 2 argument, the roots r1 and r2 of the Binary Trees. 
The struct Node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return true if both trees are identical else false.

User task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical().

Constraints:
1 <=T <= 30
1 <= Number of nodes <= 100
1 <=Data of a node <= 1000

Example:
Input
2
2
1 2 L 1 3 R
2
1 2 L 1 3 R
2
1 2 L 1 3 R
2
1 3 L 1 2 R

Output
1
0

Explanation:
Testcase 1: There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.
Testcase 2: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.
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
        tree = Tree()
        lis=[]
        root1 = None
        root1 = tree.insert(root1, int(arr[0]), 'L')
        lis.append(root1)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis=[]
        root2 = None
        root2 = tree.insert(root2, int(arr[0]), 'L')
        lis.append(root2)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k+=3
        if isIdentical(root1, root2):
            print(1)
        else:
            print(0)

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
# function should return true/false or 1/0
def isIdentical(root1, root2):
    # Code here
    if root1 == None and root2 == None:
            return True
    if root1 == None or root2 == None:
        return False
    return root1.data == root2.data and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
