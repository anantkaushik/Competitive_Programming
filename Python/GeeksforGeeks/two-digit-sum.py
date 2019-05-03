"""
You are given a two digit number n. Find the sum of its digits

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing n.

Output Format:
For each testcase, in a new line, print the sum of digits of n.

Your Task:
This is a function problem. You do not need to take any input. Complete the function digitsSum and return the sum of digits of n.

Constraints:
1 <= T <= 100
10 <= n <= 99

Example:
Input:
1
25
Output:
7
"""
{
#Initial Template for Python 3
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def digitsSum(n):
    ##Your code here
    return n%10 + n//10