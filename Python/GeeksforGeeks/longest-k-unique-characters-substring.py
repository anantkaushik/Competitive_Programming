"""
Problem Link: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

Given a string you need to print the size of the longest possible substring that has exactly K unique characters. 
If there is no possible substring then print -1.

Example 1:
Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest 
substring with K distinct characters.

Example 2:
Input: 
S = "aaaa", K = 2
Output: -1
Explanation: There's no substring with K
distinct characters.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S 
and an integer K as input and returns the length of the longest substring with exactly K distinct characters. 
If there is no substring with exactly K distinct characters then return -1.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1<=|S|<=105
1<=K<=105
"""
class Solution:

    def longestKSubstr(self, s, k):
        char_count = {}
        ans = -1
        
        start_index = 0
        for index, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            
            if len(char_count) == k:
                ans = max(ans, index - start_index + 1)
            
            if len(char_count) == k+1:
                while len(char_count) > k and start_index < index:
                    char_count[s[start_index]] -= 1
                    
                    if char_count[s[start_index]] == 0:
                        del char_count[s[start_index]]
                        
                    start_index += 1
                ans = max(ans, index - start_index + 1)
        
        return ans

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)
