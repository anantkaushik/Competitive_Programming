"""
Problem Link: https://practice.geeksforgeeks.org/problems/maximum-sum-of-elements-not-part-of-lis/1

Given an array Arr[], the task is to find the maximum sum of all the elements which are not a part of the longest 
increasing subsequence.

Example 1:
Input:
n = 6
Arr = {4, 6, 1, 2, 4, 6}
Output: 10
Explaination: Elements are 4 and 6.

Example 2:
Input:
n = 5
Arr = {5, 4, 3, 2, 1}
Output: 14
Explaination: Elements are 5,4,3 and 2.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSumLis() which takes the 
array Arr[] and its size n as input parameters and returns maximum sum of elements not part of LIS.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ N ≤ 1000
1 ≤ Arr[i] ≤ 105
"""
class Solution:
    def maxSumLis(self, arr, n):
        total_sum = sum(arr)
        
        dp = [[1, num] for num in arr]
        
        res = min(dp)
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    temp = [dp[j][0] + 1, dp[j][1] + arr[i]]
                    
                    if temp[0] > dp[i][0]:
                        dp[i] = temp
                    elif temp[0] == dp[i][0]:
                        dp[i][1] = min(temp[1], dp[i][1])
                    
            if res[0] < dp[i][0]:
                res = dp[i]
            elif res[0] == dp[i][0]:
                res = min(res, dp[i])
        
        return total_sum - res[1]
