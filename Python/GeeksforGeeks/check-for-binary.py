"""
Problem Link: https://practice.geeksforgeeks.org/problems/check-for-binary/1
     
Given a non-empty sequence of characters, return true if sequence is Binary, else return false

Input:
The task is to complete the method that takes a string as argument. We should not read any input from stdin/console. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
Your function should return true str is binary, else false

Constraints:
1<=T<=50
1<=Length of str<=10000

Example:

Input:
2
101
75

Output:
1
0
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)

def isBinary(str):
    for i in str:
        if i not in "01":
            return False
    return True