"""
Problem Link: https://practice.geeksforgeeks.org/problems/preorder-traversal/1

Given a binary tree, find its preorder traversal.

Example 1:
Input:
        1      
      /          
    4    
  /    \   
4       2
Output: 1 4 4 2 

Example 2:
Input:
       6
     /   \
    3     2
     \   / 
      1 2
Output: 6 3 1 2 2 

Your Task:
You just have to complete the function preorder() which takes the root 
node of the tree as input and returns an array containing the preorder 
traversal of the tree.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 104
0 <= Data of a node <= 105
"""
def preorder_iterative(root):
    res = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
                
    return res


def preorder(root, res=None):
  if not root:
      return res
   
  if not res:
      res = []
  res.append(root.data)
  preorder(root.left, res)
  preorder(root.right, res)
  return res
