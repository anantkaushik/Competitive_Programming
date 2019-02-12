"""
Problem Link: https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1

Given an array of size N which represents the elements to be inserted into BST (considering first element as root). 
The task is to find the minimum element in this given BST. If the tree is empty, there is no minimum elemnt, 
so print -1 in that case.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. 
The first line contains N (number of nodes in BST). The second line contains N nodes of the BST separated by space.

Output:
For each testcase in new line, print the minimum element in BST.

User Task:
The task is to complete the function minValue() which takes root as the argument and returns the minimum element of BST.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
2
6
5 4 3 6 7 1
3
9 10 11

Output:
1
9

Explanation:
Testcase 1: The minimum value in the given BST is 1.
"""
#Initial Template for Python 3
class Node:
    data=0
    left=None
    right=None
def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    
def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root
    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
        print(minValue(root))
        testcases-=1
if __name__=="__main__":
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
##Structure of the node
'''
class Node:
    data=0
    left=None
    right=None
'''
##Complete this function
def minValue(root):
    ##Your code here
    while root.left:
        root = root.left
    return root.data