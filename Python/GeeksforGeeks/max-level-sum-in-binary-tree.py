"""
Problem Link: https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1/

Given a Binary Tree having positive and negative nodes. 
Find the maximum sum of a level in the given Binary Tree.

Example 1:
Input :               
             4
          /    \
         2     -5
        / \    / \
      -1   3  -2  6
Output: 6
Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 2'th level is 6
Hence maximum sum is 6

Example 2:
Input :          
            1
          /   \
         2     3
        / \     \
       4   5     8
                / \
               6   7  
Output :  17

Explanation: Maximum sum is at level 2.

Your Task:  
You dont need to read input or print anything. Complete the function 
maxLevelSum() which takes root node as input parameter and 
returns the maximum sum of any horizontal level in the given Binary Tree.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""
class Solution:
    def maxLevelSum(self, root):
        return max(self.helper(root))
        
    def helper(self, root, level=0, levels_sum=None):
        if not root:
            return 0
            
        if not levels_sum:
            levels_sum = []
        if level == len(levels_sum):
            levels_sum.append(0)
        
        levels_sum[level] += root.data
        
        self.helper(root.left, level+1, levels_sum)
        self.helper(root.right, level+1, levels_sum)
        return levels_sum
