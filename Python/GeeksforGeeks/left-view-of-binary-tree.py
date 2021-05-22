"""
Problem Link: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited 
from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:
Input:
   1
 /  \
3    2
Output: 1 3

Example 2:
Input:
Output: 10 20 40

Your Task:
You just have to complete the function leftView() that prints the left view. The newline is automatically appended by the 
driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000
"""
# DFS
def LeftViewDFS(root):
    
    def helper(root, level, res):
        if not root:
            return res
    
        if level > len(res):
            res.append(root.data)
        
        helper(root.left, level+1, res)
        helper(root.right, level+1, res)
        
        return res
    
    return helper(root, 1, [])
        
# BFS
def LeftView(root):
    if not root:
		return []
		
	level = [root]
	res = []
	
	while level:
		for index in range(len(level)):
			node = level.pop(0)
			if index == 0:
				res.append(node.data)
			
			if node.left:
				level.append(node.left)
			if node.right:
				level.append(node.right)
				
	return res
