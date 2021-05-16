"""
Problem Link: https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1

Given a gold mine called M of (n x m) dimensions. Each field in this mine contains a positive integer which is the amount 
of gold in tons. Initially the miner can start from any row in the first column. From a given cell, the miner can move
to the cell diagonally up towards the right 
to the right
to the cell diagonally down towards the right
Find out maximum amount of gold which he can collect.

Example 1:
Input: n = 3, m = 3
M = {{1, 3, 3},
     {2, 1, 4},
     {0, 6, 4}};
Output: 12

Explaination: 
The path is {(1,0) -> (2,1) -> (2,2)}.

Example 2:
Input: n = 4, m = 4
M = {{1, 3, 1, 5},
     {2, 2, 4, 1},
     {5, 0, 2, 3},
     {0, 6, 1, 2}};
Output: 16
Explaination: 
The path is {(2,0) -> (3,1) -> (2,2) 
-> (2,3)} or {(2,0) -> (1,1) -> (1,2) 
-> (0,3)}.

Your Task:
You do not need to read input or print anything. Your task is to complete the function maxGold() which takes the 
values n, m and the mine M as input parameters and returns the maximum amount of gold that can be collected.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 50
1 ≤ M[i][j] ≤ 100
"""
class Solution:
    def maxGold(self, n, m, M):
        cache = [[0] * m for _ in range(n)]
        
        directions = [[0, 1], [-1, 1], [1, 1]]
        
        max_gold = 0
        for col in range(m-1, -1, -1):
            for row in range(n-1, -1, -1):
                max_val = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    
                    if not (new_row >= 0 and new_row < n and new_col < m):
                        continue
                    
                    max_val = max(max_val, cache[new_row][new_col])
                
                cache[row][col] = M[row][col] + max_val
                
                if col == 0:
                    max_gold = max(max_gold, cache[row][col])
        
        return max_gold


class Solution1:
    def maxGold(self, n, m, M):
        cache = [[0] * m for _ in range(n)]
        
        directions = [[0, 1], [-1, 1], [1, 1]]
        queue = []
        for row in range(n):
            queue.append([row, 0, M[row][0]])
        
        max_gold = 0
        while queue:
            
            for _ in range(len(queue)):
                row, col, cur_gold = queue.pop(0)
                cache[row][col] = cur_gold
                max_gold = max(max_gold, cur_gold)
            
                for direction in directions:
                    next_row = row + direction[0]
                    next_col = col + direction[1]
                    if not (next_row >= 0 and next_row < n and next_col < m and cache[next_row][next_col] < cur_gold + M[next_row][next_col]):
                        continue
                    
                    queue.append([next_row, next_col, cur_gold + M[next_row][next_col]])
            
        return max_gold
