"""
Problem Link: https://practice.geeksforgeeks.org/problems/level-order-traversal/1

Level order traversal of a tree is breadth-first traversal for the tree. 

Input:
The task is to complete the method which takes one argument, root of Binary Tree. 
The struct Node has a data part which stores the data, pointer to left child and pointer to the right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print the level order traversal of the tree as specified in the problem statement.

Constraints:
1 <=T<= 20
1 <= Number of edges<= 1000
1 <= Data of a node<= 100

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
1 3 2
10 20 30 40 60
 
There are two test cases.  The first case represents a tree with 3 nodes and 2 edges where the root is 1, 
left child of 1 is 3 and right child of 1 is 2. Second test case represents a tree with 4 edges and 5 nodes.
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Tree:
    def createNode(self, data):
        return Node(data)
            
    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.data, end=' ')
            self.traverse(root.right)
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = {}
        root = None
        root = tree.createNode(int(arr[0]))
        lis[root.data]=root
        k=0
        for j in range(n):
            if int(arr[k]) in lis:
                ptr = tree.createNode(int(arr[k+1]))
                if arr[k+2]=='L':
                    lis[int(arr[k])].left = ptr
                else:
                    lis[int(arr[k])].right = ptr
                lis[int(arr[k+1])] = ptr
                k+=3
        traverse_level_order(root)
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree
def traverse_level_order( root ):
    # Code here
    q = [root]
    while q:
        temp = q.pop(0)
        print(temp.data,end=' ')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        