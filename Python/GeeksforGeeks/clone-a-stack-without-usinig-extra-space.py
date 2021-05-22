"""
Problem Link: https://practice.geeksforgeeks.org/problems/clone-a-stack-without-usinig-extra-space/1

Given elements of a stack, clone the stack without using extra space.

Example 1:
Input:
N = 10
st[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
Output:
1 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function clonestack() which takes the input stack 
st[], an empty stack cloned[], you have to clone the stack st into stack cloned.
The driver code itself prints 1 in the output if the stack st is cloned properly and prints 0 otherwise.

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 1000
1<= st[i] <= 105
"""
class Solution:
    def clonestack(self, st, cloned):
        length = len(st)
        for i in range(length-1):
            val = st.pop()
            
            for _ in range(len(st) - i):
                cloned.append(st.pop())
            
            st.append(val)
            while cloned:
                st.append(cloned.pop())
        
        while st:
            cloned.append(st.pop())
