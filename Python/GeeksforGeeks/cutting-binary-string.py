"""
Problem Link: https://practice.geeksforgeeks.org/problems/cutting-binary-string1342/1

Given a string s containing 0's and 1's. You have to return a smallest positive integer C, 
such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.

Example 1:
Input:
s = "101101101"
Output: 3
Explanation: We can split the given string
             into three “101”s, where 101 is
             the binary representation of 5.

Example 2:
Input:
s = "00000"
Output: -1
Explanation: 0 is not a power of 5.

Your Task:
Your task is to complete the function cuts() which take a single argument(string s) and return C. 
You need not take any input or print anything.
Expected Time Complexity: O(|s|*|s|*|s|).
Expected Auxiliary Space: O(|s|).

Constraints:
1<=s.length()<=50
Note: The string s is a binary string.
"""
import math

class Solution:

    def cuts(self, s):
        
        dp = [[False] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            cur_str = ""
            for j in range(i, len(s)):
                cur_str += s[j]
                if cur_str == "1":
                    dp[i][j] = True
                else:
                    dp[i][j] = self.is_power(cur_str, 5)
        
        stack = []
        for i in range(len(s)):
            if dp[0][i]:
                stack.append([i+1, 1])
        
        # print(stack)
        res = float('inf')
        while stack:
            index, level = stack.pop()
            # print(index, level)
            
            if index == len(s):
                res = min(level, res)
                continue
            
            for i in range(index, len(s)):
                if dp[index][i]:
                    stack.append([i+1, level + 1])
        
        return res if res != float('inf') else -1
                
    
    
    def is_power(self, x, y):
        if x[0] == "0":
            return False
            
        x = int(x, 2)
        if x < y:
            return False
            
        s = math.log(x, y)
        p = round(s)
        return y**p == x

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.cuts(s))

# } Driver Code Ends