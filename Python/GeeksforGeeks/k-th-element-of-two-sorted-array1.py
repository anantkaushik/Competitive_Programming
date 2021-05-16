"""
Problem Link: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

Given two sorted arrays arr1 and arr2 of size M and N respectively and an element K. The task is to find the element that 
would be at the k’th position of the final sorted array.

Example 1:
Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5
Output:
6
Explanation:
The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.

Example 2:
Input:
arr1[] = {100, 112, 256, 349, 770}
arr2[] = {72, 86, 113, 119, 265, 445, 892}
k = 7
Output:
256
Explanation:
Final sorted array is - 72, 86, 100, 112,
113, 119, 256, 265, 349, 445, 770, 892
7th element of this array is 256.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function kthElement() 
which takes the arrays arr1[], arr2[], its size N and M respectively and an integer K as inputs and returns the element 
at the Kth position.

Expected Time Complexity: O(Log(N) + Log(M))
Expected Auxiliary Space: O(Log (N))

Constraints:
1 <= N, M <= 106
1 <= arr1i, arr2i <= 106
1 <= K <= N+M
"""
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if m < n:
            return self.kthElement(arr2, arr1, m, n, k)
            
        k -= 1
        arr1_index = 0
        arr2_index = 0
        
        while arr1_index < n and arr2_index < m:
            k -= 1
            
            if arr1[arr1_index] < arr2[arr2_index]:
                arr1_index += 1
            else:
                arr2_index += 1
            
            if k == 0:
                return min(arr1[arr1_index] if arr1_index < n else float('inf'), arr2[arr2_index] if arr2_index < m else float('inf'))
        
        return arr2[arr2_index + k] 
