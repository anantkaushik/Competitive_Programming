"""
Problem Link: https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1

Input:
N = 3
Output: 5
Explanation: 5 strings are (000,
001, 010, 100, 101).

Example 2:
Input:
N = 2
Output: 3
Explanation: 3 strings are
(00,01,10).

Your Task:
Complete the function countStrings() which takes single integer n, as input parameters and returns an integer denoting the answer. 
You don't to print answer or take inputs. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
"""
class Solution:

	def countStrings(self,n):
	    zero_count = 1
	    one_count = 1
	   
	    for i in range(1, n):
	        zero_count, one_count = (zero_count + one_count) % 1000000007, zero_count
	    
	    return (zero_count + one_count) % 1000000007


# TLE
class Solution1:

    def countStrings(self,n):
        return len(self.helper(n))
        
    def helper(self, n):
        if n == 1:
            return ["0", "1"]
        numbers = self.helper(n-1)
        res = []
        for num in numbers:
            res.append(num + "0")
            if num[-1] != "1":
                res.append(num + "1")
        return res
