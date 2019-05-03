"""
Problem Link: https://practice.geeksforgeeks.org/contest-problem/nearest-power/1/

You are given two numbers a and b. When a is raised to some power p, we get a number x. Now, you need to find what is the 
value of x that is closest to b.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. 
The first line contains a and second line contains b.

Output Format:
For each testcase, in a new line, print the closest power.

Your Task:
This is a function problem. You do not need to take any input. Complete the function nearestPower and return the answer.

Constraints:
1 <= T <= 100
2 <= a <= 100
a <= b <= 108

Example:
Input:
1
2
4
Output:
4

Explanation:
Testcase1: 22=4 is closest to 4
"""
#Initial Template for Python 3
import math
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        print(nearestPower(a,b))
        testcases-=1
        
if __name__=='__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
    
def nearestPower(a,b):
    x = math.floor(math.log(b,a))
    n1 = a**x
    n2 = a**(x+1)
    return n2 if(abs(n1-b)>abs(n2-b)) else n1