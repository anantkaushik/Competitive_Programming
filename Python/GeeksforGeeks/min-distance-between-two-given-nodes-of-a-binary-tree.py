"""
Problem Link: https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1#

Given a binary tree and two node values your task is to find the minimum distance between them.

Example 1:
Input:
        1
      /  \
     2    3
a = 2, b = 3
Output: 2
Explanation: The tree formed is:
       1
     /   \ 
    2     3

We need the distance between 2 and 3.
Being at node 2, we need to take two
steps ahead in order to reach node 3.
The path followed will be:
2 -> 1 -> 3. Hence, the result is 2. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function findDist() which takes the root node 
of the Tree and the two node values a and b as input parameters and returns the minimum distance between the nodes 
represented by the two given node values.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 104
1 <= Data of a node <= 105
Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for 
Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. 
The task is to complete the function specified, and not to write the full code.
"""
#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def findDist(root,a,b):
    
    
    def find_node(root, val, parents):
        if not root:
            return []
        
        if root.data == val:
            parents.append(root.data)
            return parents
            
        return find_node(root.left, val, parents + [root.data]) or find_node(root.right, val, parents + [root.data])
    
    a_parents = find_node(root, a, [])
    b_parents = find_node(root, b, [])

    index = 0
    
    while index < len(a_parents) and index < len(b_parents):
        if a_parents[index] != b_parents[index]:
            break
        index += 1
        
    return (len(a_parents) - index) + (len(b_parents) - index)
        
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        print(findDist(root, a, b))

# } Driver Code Ends