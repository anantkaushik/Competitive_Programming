"""
Problem Link: https://practice.geeksforgeeks.org/problems/count-increasing-subsequences3134/1

Given an array of digits (values lie in range from 0 to 9). The task is to count all the sub sequences possible in array 
such that in each subsequence every digit is greater than its previous digits in the subsequence.

Example 1:
Input : 
a[] = {1, 2, 3, 4}
Output: 
15
Explanation :
There are total increasing subsequences
{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4},
{2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4},
{1,3,4}, {2,3,4}, {1,2,3,4}
 

Example 2:
Input : 
a[] = {4, 3, 6, 5}
Output:
8
Explanation :
Sub-sequences are {4}, {3}, {6}, {5},
{4,6}, {4,5}, {3,6}, {3,5}
 
Example 3:
Input : 
a[] = {3, 2, 4, 5, 4}
Output : 
14
Explanation :
Sub-sequences are {3}, {2}, {4}, {3,4},
{2,4}, {5}, {3,5}, {2,5}, {4,5}, {3,2,5}
{3,4,5}, {4}, {3,4}, {2,4}

Your Task:
You don't have to print anything, printing is done by the driver function. You have to complete the function countSub() 
which takes the array a[] and its size N as inputs and returns the count of all increasing subsequences in given array of digits.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O( max(a[i]) ) = O(10)

Constraints:
1 ≤ N ≤ 500
1 ≤ a[i] ≤ 9
"""
# O(N)
class Solution:
    def countSub(self, arr, n):
        count = [0] * 10
        
        for i in range(n):
            for j in range(arr[i]-1, -1, -1):
                count[arr[i]] += count[j]
            
            count[arr[i]] += 1
            
        return sum(count)


# O(N*N)
class Solution1:
    def countSub(self, arr, n):
        dp = [1] * n
        
        total_sum = 1
        for i in range(1, n):
            for j in range(i+1):
                if arr[j] < arr[i]:
                    dp[i] += dp[j]
                    
            total_sum += dp[i]
            
        return total_sum