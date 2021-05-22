"""
Problem Link: https://practice.geeksforgeeks.org/problems/doubling-the-value4859/1

Given an array and an integer B, traverse the array (from the beginning) and if the element in array is B, 
double B and continue traversal. Find the value of B after the complete traversal.

Example 1:
Input:
N = 5, B = 2
arr[] = {1 2 3 4 8}
Output: 16
Explanation: B is initially 2. We get 2 at
the 1st index, hence B becomes 4. 
Next, we get B at the 3rd index, hence B 
becomes 8. Next, we get B at 4-th index, 
hence B becomes 16.

Example 1:
Input:
N = 5, B = 3
arr[] = {1 2 3 4 8}
Output: 6
Explanation: B is initially 3. We get 3 at
the 2nd index, hence B becomes 6.

Your Task:
You don't need to read input or print anything. Your task is to complete the function solve () which takes the array arr[], 
its size N and an integer B as inputs and returns the final value of B after the complete traversal of the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1<=N<=50
1<=B<=1000
1<=arr[i]<=1018
"""
class Solution:
    def solve(self,n : int, a : list, b : int):
        for num in a:
            if num == b:
                b *= 2
        
        return b
