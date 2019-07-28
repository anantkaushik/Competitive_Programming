"""
Problem Link: https://practice.geeksforgeeks.org/problems/postorder-traversal/1

Given a binary tree, print postorder traversal of it. Postorder traversal of below tree is 5 10 39 1

        1
     /     \
   10     39
  /
5

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. 
The first line contains number of edges. The second line contains the connections between the nodes.

Output Format:
For each testcase, in a new line, print the postorder traversal.

Your Task:
You don't need to take input. Just complete the function postorder() that takes node as parameter. The newline is automatically 
appended by the driver code.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
3 2 1
40 60 20 30 10

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, the postorder would be 3 2 1
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the postorder would be 40 60 20 30 10.
"""
{
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict # default dict used as a map, to store node-value mapping.
#Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        postOrder(tree.root)
        print()

}
''' This is a function problem.You only need to complete the function given below '''

#User function Template for python3
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def postOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated post order Traversal of the given tree.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    # code here
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")