class Solution(object):
    def longestPalindrome(self, s):
        def func(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left=left-1
                right=right+1
            return s[left+1:right]
        
        res=""
        for i in range(len(s)):
            test=func(i,i)
            if len(test)>len(res):
                res=test
            test=func(i,i+1)
            if len(test)>len(res):
                res=test
        return res
