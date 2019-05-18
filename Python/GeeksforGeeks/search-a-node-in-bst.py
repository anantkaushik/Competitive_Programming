"""
Problem Link: https://practice.geeksforgeeks.org/problems/search-a-node-in-bst/1

Given a Binary Search Tree (BST), you need to find if a particular node(data) is present in the BST or not. If present print 1, 
else print 0.

Input Format:
The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. 
Each test case consists of three lines. Description of  test cases is as follows:
The First line of each test case contains an integer 'N' which denotes the no of nodes to be inserted in the BST.
The Second line of each test case contains 'N' space separated values denoting the values of the BST.
In the third line is an integer x denoting the node to be searched for.

Output Format:
The output for each test case will be 1 if the node is present in the BST else 0.

Your Task:
This is a function problem. you don't have to read any input. Your task is to complete the function search which returns true 
if the node with value x is present in the BST else returns false.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input
2
7
2 81 87 42 66 90 45 
87
4
6 7 9 8
11
Output
1
0
"""
{
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node
    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        num = int(input())
        find = gfg()
        if find.search(root, num):
            print(1)
        else:
            print(0)
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Function should return True/False or 1/0
class gfg:
    def search(self, node, data):
        #code here
        if not node:
            return False
        if node.data == data:
            return True
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)