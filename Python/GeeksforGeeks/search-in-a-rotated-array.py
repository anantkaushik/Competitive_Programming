"""
Problem Link: https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1

Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. 
The task is to find the index of the given element key in the array A.

Example 1:
Input:
N = 9
A[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}
key = 10
Output:
5
Explanation: 10 is found at index 5.

Example 2:
Input:
N = 4
A[] = {3, 5, 1, 2}
key = 6
Output:
-1
Explanation: There is no element that has value 6.

Your Task:
Complete the function search() which takes an array arr[] and start, end index of the array and the K as input parameters, 
and returns the answer.
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
0 ≤ A[i] ≤ 108
1 ≤ key ≤ 108
"""
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
	    while l < h:
            mid = (l+h)//2
            
            if A[mid] == key:
                return mid
            if A[l] < A[h]:
                if A[mid] < key:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if (A[mid] < A[h] and (key <= A[h] and key > A[mid])) or (A[mid] > A[h] and (key <= A[h] or key > A[mid])):
                    l = mid + 1
                else:
                    h = mid - 1
        
        return l if A[l] == key else -1
