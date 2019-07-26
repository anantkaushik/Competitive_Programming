"""
Problem Link: https://practice.geeksforgeeks.org/problems/the-counting-game/0

Given a string S of lowercase aplhabets, check if it is isogram or not. An Isogram is a string in which no letter occurs more than once.

Input Format:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each test case consist of one string in 
'lowercase' only, in a separate line.

Output Format:
For each testcase, in a new line, Print 1 if string is Isogram else print 0.

Your Task:
This is a function problem. You only need to complete the function isIsogram() that takes string as parameter and returns either true or false.

Constraints:
1 <= T <= 100
1 <= |S| <= 103

Example:
Input:
2
machine
geeks
Output:
1
0

Explanation:
Testcase 2: geeks is not an isogram as 'e' appears twice. Hence we print 0.
"""
{
#Initial Template for Python 3
def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        if isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1
if __name__=="__main__":
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
def isIsogram(s):
    #Your code here
    temp = set()
    for c in s:
        if c in temp:
            return False
        temp.add(c)
    return True