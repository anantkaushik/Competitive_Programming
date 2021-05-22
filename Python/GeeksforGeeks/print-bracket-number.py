"""
Problem Link: https://practice.geeksforgeeks.org/problems/print-bracket-number4058/1

Given a string S, the task is to find the bracket numbers. 

Example 1:
Input:  S = "(aa(bdc))p(dee)â€‹"
Output: 1 2 2 1 3 3
Explanation: The highlighted brackets in
the given string (aa(bdc))p(dee) has been 
assigned the numbers as: 1 2 2 1 3 3.

Example 2:
Input:  S = "(((()("
Output: 1 2 3 4 4 5
Explanation: The highlighted brackets in
the given string (((()( has been assigned
the numbers as: 1 2 3 4 4 5

User Task:
Your task is to complete the function barcketNumbers() which takes a single string as input and returns a list of numbers. 
You do not need to take any input or print anything.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1 <= |S| <= 105
S contains lower case English alphabets, and '(', ')' characters
At any time the number of opening brackets are greater than closing brackets
"""
class Solution:
	def barcketNumbers(self, S):
		stack, res = [], []
		count = 0
		
		for c in S:
			if c ==  "(":
				count += 1
				stack.append(count)
				res.append(count)
			elif c == ")":
				c = stack.pop()
				res.append(c)

		return res
