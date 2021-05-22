"""
Problem Link: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the 
knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N 
items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] 
such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the 
complete item, or don’t pick it (0-1 property).

Example 1:
Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3

Example 2:
Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0

Your Task:
Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[] and number of items 
n as a parameter and returns the maximum possible value you can get.
Expected Time Complexity: O(N*W).
Expected Auxiliary Space: O(N*W)
Constraints:
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000
"""
# Time Complexity -> O(N*W)
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[0] * (W+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]

# Time Complexity -> O(N*W)
class Solution1:
    
    def knapSack(self,W, wt, val, n):
        self.cache = {}
        
        def helper(w, wt, val, index):
            
            if index == -1 or w == 0:
                return 0
            
            if (w, index) not in self.cache:
                if w >= wt[index]:
                    self.cache[w, index] = max(val[index] + helper(w-wt[index], wt, val, index-1), helper(w, wt, val, index-1))
                else:
                    self.cache[w, index] = helper(w, wt, val, index-1)
            
            return self.cache[w, index]
        
        return helper(W, wt, val, n-1)

# TLE
# Time Complexity -> O(2^N)
class Solution2:
    
    def knapSack(self,W, wt, val, n):
        
        def helper(w, wt, val, index):
            if index == -1 or w == 0:
                return 0
            if w >= wt[index]:
                return max(val[index] + helper(w-wt[index], wt, val, index-1), helper(w, wt, val, index-1))
            return helper(w, wt, val, index-1)
        
        return helper(W, wt, val, n-1)
