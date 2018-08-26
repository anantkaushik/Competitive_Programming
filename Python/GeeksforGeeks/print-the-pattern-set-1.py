"""
Problem Link = "https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1"
Your task is to complete the function printPat which takes one argument 'n' denoting the length of the pattern and prints the 
following pattern
for n=2 the pattern will be 
2 2 1 1
2 1
for n=3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Input:
The first line of input is the number of test cases .  The T test cases follow . The first line of each test case is an integer N.

Output:
For each test case print the required pattern in a single line . 
Note : Instead of printing new line print a "$" without quotes.

Constraints:
1<=T<=20
1<=N<=40

Example:
Input
1
2
3
Output
2 2 1 1 $2 1 $
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $


Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. 
As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, 
and not to write the full code.
"""

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))

def printPat(n):
    result = ""
    for i in range(n,0,-1):
        t = []
        for j in range(n,0,-1):
            t.extend([str(j)]*i)
        result+=" ".join(t)
        result+=" $"
    return result